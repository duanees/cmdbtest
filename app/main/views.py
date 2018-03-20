#coding=utf-8
from flask import render_template,redirect,url_for,session,g,request
from app.main import main
from flask_login import login_required
from app import login_manager
from app.models import *
from app import util
import uuid
import socket
import struct
import math
from app.main import forms
from app import function
from app.main import filters

ROW_COUNT = 15

thead_list = ["序号","资产类型","资产位置","主机名","资产型号","资产编号","资产序列号","IPCode","业务IP","管理IP","所属部门","资产接口人","归属项目","项目合同","终验时间","状态","下架评估","CPU配置","内存配置","硬盘配置","CPU使用率","内存使用率","硬盘使用率","备注"]

@main.route('/')
@login_required
def index():
    return render_template("index.html")



@main.route('/inventory/',methods = ["GET","POST"])
def inventory():
    form = forms.SearchForm()
    page = int(request.args.get("page",1))
    word = request.args.get('q')
    kwargs = {
        'page':(page - 1) * ROW_COUNT,
        'row_count': ROW_COUNT
    }
    datas = []
    datas,count = util.list_search(word,**kwargs)
    total = int(math.ceil(count/(ROW_COUNT * 1.0)))
    dic_list = function.get_page(total,page)
    page_dict = {'page':page,'total':total,'dic_list':dic_list}
    return render_template("inventory.html",datas=datas,thead_list=thead_list,page_dict=page_dict,form=form)

@main.route('/inventory/create',methods=['GET','POST'])
def create():
    form = forms.CreateForm()
    if form.validate_on_submit():
        kwargs = {}
        ip_kwargs = {}
        kwargs['type'] = form.type.data
        kwargs['idc'] = form.idc.data
        kwargs['cabinet'] = form.cabinet.data
        if form.addresses.data:
            kwargs['addresses'] = int(form.addresses.data)
        kwargs['host_name'] = form.host_name.data
        kwargs['model'] = form.model.data
        kwargs['asset_code'] = form.asset_code.data
        kwargs['asset_sn'] = form.asset_sn.data
        if form.ip_business.data:
            ip_business_code = uuid.uuid4()
            kwargs['ip_business_code'] = ip_business_code
            ip_kwargs['ip_business_code'] = ip_business_code
            ip_value = socket.ntohl(struct.unpack("I", socket.inet_aton(str(form.ip_business.data)))[0])
            ip_kwargs['ip_value'] = ip_value
        if form.ip_admin.data:
            ip_admin = socket.ntohl(struct.unpack("I", socket.inet_aton(str(form.ip_admin.data)))[0])
            kwargs['ip_admin'] = ip_admin
        kwargs['department'] = form.department.data
        kwargs['interfac_person'] = form.interfac_person.data
        kwargs['project'] = form.project.data
        kwargs['project_contract'] = form.project_contract.data
        kwargs['project_acceptance_time'] = form.project_acceptance_time.data
        kwargs['state'] = form.state.data
        kwargs['off_shelf_evaluation'] = form.off_shelf_evaluation.data
        kwargs['cpu_config'] = form.cpu_config.data
        kwargs['memory_config'] = form.memory_config.data
        kwargs['disk_config'] = form.disk_config.data
        kwargs['cpu_use_rate'] = form.cpu_use_rate.data
        kwargs['memory_use_rate'] = form.memory_use_rate.data
        kwargs['disk_use_rate'] = form.disk_use_rate.data
        kwargs['remark'] = form.remark.data
        util.insert_inventory(**kwargs)
        util.insert_inventory_ip(**ip_kwargs)
        return redirect(url_for('main.inventory'))
    return render_template("inventory/create.html", form=form)

@main.route('/inventory/delete',methods=['GET','POST'])
def delete():
    serial_no_str = request.args.get("serial_nos", '')
    serial_nos = serial_no_str.split('|')
    serial_nos = [int(num) for num in serial_nos]
    util.delete_inventory(serial_nos)
    util.delete_inventory_ip(serial_nos)
    return redirect(url_for('main.inventory'))

@main.route('/inventory/update',methods=['GET','POST'])
def update():
    serial_nos = int(request.args.get("serial_nos", 1))
    inventory = util.get_inventory()
    form = forms.UpdateForm(inventory)
    return redirect(url_for('main.inventory'))



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@main.before_request
def beforelogin():
    user_id = session.get('user_id')
    user = util.get_user(user_id)
    g.user = user

@main.context_processor
def my_processor():
    if g.user:
        return {'user':g.user}
    else:
        return {}