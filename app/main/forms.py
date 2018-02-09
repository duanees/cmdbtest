#coding=utf-8
from flask_wtf import Form,FlaskForm
from wtforms.validators import Length, Email,DataRequired
from wtforms import StringField, IntegerField, SubmitField,SelectField,DateTimeField,validators
from app import util

class SearchForm(Form):
  search = StringField('search', validators=[DataRequired()])

class CreateForm(Form):
    type = SelectField('类型', validators=[DataRequired()], coerce=int)
    idc = SelectField('资产位置', coerce=int)
    cabinet = StringField('机柜',render_kw={'placeholder':'IDC5-G01'})
    addresses = StringField('U数', render_kw={'placeholder':'3743'})
    host_name = StringField('主机名', render_kw={'placeholder':''})
    model = StringField('资产型号')
    asset_code = StringField('资产编号')
    asset_sn = StringField('资产序列号')
    ip_business = StringField('业务IP')
    ip_admin = StringField('管理IP')
    department = SelectField('所属部门', coerce=int)
    interfac_person = StringField('资产接口人')
    project = StringField('归属项目')
    project_contract = StringField('项目合同')
    project_acceptance_time = DateTimeField('终验时间', format='%Y-%d-%m', validators=(validators.Optional(),))
    state = SelectField('状态', coerce=int)
    off_shelf_evaluation = SelectField('下架评估', coerce=int)
    cpu_config = StringField('CPU配置')
    memory_config = StringField('内存配置')
    disk_config = StringField('	硬盘配置')
    cpu_use_rate = IntegerField('CPU使用率',validators=(validators.Optional(),))
    memory_use_rate = IntegerField('内存使用率',validators=(validators.Optional(),))
    disk_use_rate = IntegerField('硬盘使用率',validators=(validators.Optional(),))
    remark = StringField('备注')
    submit = SubmitField('添加')

    def __init__(self, *args, **kwargs):
        super(CreateForm, self).__init__(*args, **kwargs)
        self.departments = util.list_department()
        self.type.choices = [(1, '服务器设备'),(2,'存储设备'),(3, '网络设备'), (4, '传输设备')]
        self.idc.choices = [( 1,'转塘'),( 2,'三墩'),(3, '白马湖')]
        self.department.choices = [(dep.department_id, dep.department) for dep in self.departments]
        self.state.choices = [( 1, '开机'), (4,'关机')]
        self.off_shelf_evaluation.choices = [( 1,'不下架'),(4,'下架')]

class UpdateForm(Form):
    type = SelectField('类型', validators=[DataRequired()], coerce=int)
    idc = SelectField('资产位置', coerce=int)
    cabinet = StringField('机柜',render_kw={'placeholder':'IDC5-G01'})
    addresses = StringField('U数', render_kw={'placeholder':'3743'})
    host_name = StringField('主机名')
    model = StringField('资产型号')
    asset_code = StringField('资产编号')
    asset_sn = StringField('资产序列号')
    ip_business = StringField('业务IP')
    ip_admin = StringField('管理IP')
    department = SelectField('所属部门', coerce=int)
    interfac_person = StringField('资产接口人')
    project = StringField('归属项目')
    project_contract = StringField('项目合同')
    project_acceptance_time = DateTimeField('终验时间', format='%Y-%d-%m', validators=(validators.Optional(),))
    state = SelectField('状态', coerce=int)
    off_shelf_evaluation = SelectField('下架评估', coerce=int)
    cpu_config = StringField('CPU配置')
    memory_config = StringField('内存配置')
    disk_config = StringField('	硬盘配置')
    cpu_use_rate = IntegerField('CPU使用率',validators=(validators.Optional(),))
    memory_use_rate = IntegerField('内存使用率',validators=(validators.Optional(),))
    disk_use_rate = IntegerField('硬盘使用率',validators=(validators.Optional(),))
    remark = StringField('备注')
    submit = SubmitField('添加')

    def __init__(self, *args, **kwargs):
        super(UpdateForm, self).__init__(*args, **kwargs)
        self.departments = util.list_department()
        self.type.choices = [(1, '服务器设备'),(2,'存储设备'),(3, '网络设备'), (4, '传输设备')]
        self.idc.choices = [( 1,'转塘'),( 2,'三墩'),(3, '白马湖')]
        self.department.choices = [(dep.department_id, dep.department) for dep in self.departments]
        self.state.choices = [( 1, '开机'), (4,'关机')]
        self.off_shelf_evaluation.choices = [( 1,'不下架'),(4,'下架')]