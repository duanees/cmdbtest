from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from sqlalchemy import Column,Integer,String,DATETIME,TIMESTAMP,DATE,func
from sqlalchemy.ext.declarative import declarative_base
from app import db

#Base = declarative_base()

class User(db.Model,UserMixin):
    __tablename__ = 'idc_asset_inventory_user'
    dgdh = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50),unique=True,nullable=False)
    password_hash = db.Column(db.String(256),nullable=False)

    @property
    def password(self):
        raise AttributeError("password is not readable attribute")

    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        result = check_password_hash(self.password_hash,password)
        return result

class Inventory(db.Model):
    __tablename__ = "idc_asset_inventory"
    serial_no = db.Column(db.Integer,primary_key=True,autoincrement=True)
    type = db.Column(db.Integer,default=1)
    idc = db.Column(db.Integer)
    cabinet = db.Column(db.String(20))
    addresses = db.Column(db.Integer)
    host_name = db.Column(db.String(100))
    model = db.Column(db.String(50))
    asset_code = db.Column(db.String(20))
    asset_sn = db.Column(db.String(20))
    ip_business_code = db.Column(db.String(50))
    ip_admin = db.Column(db.String(50))
    department = db.Column(db.String(20))
    interfac_person = db.Column(db.String(10))
    project = db.Column(db.String(50))
    project_contract = db.Column(db.String(20))
    project_acceptance_time = db.Column(db.DateTime)
    state = db.Column(db.Integer)
    off_shelf_evaluation = db.Column(db.Integer)
    cpu_config = db.Column(db.String(50))
    memory_config = db.Column(db.String(50))
    disk_config = db.Column(db.String(50))
    cpu_use_rate = db.Column(db.Integer)
    memory_use_rate = db.Column(db.Integer)
    disk_use_rate = db.Column(db.Integer)
    remark = db.Column(db.String(50))
    create_time = db.Column(db.DateTime,default=datetime.now)
    update_time = db.Column(db.TIMESTAMP, default=datetime.now,onupdate=datetime.now)
    is_delete = db.Column(db.Integer, default=0)

class Inventory_Ip(db.Model):
    __tablename__ = 'idc_asset_inventory_ip'
    serial_no = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ip_business_code = db.Column(db.String(50))
    ip_value = db.Column(db.String(50))
    create_time = db.Column(db.DateTime,default=datetime.now)
    update_time = db.Column(db.TIMESTAMP, default=datetime.now,onupdate=datetime.now)
    is_delete = db.Column(db.Integer, default=0)

class ActionView(db.Model):
    __tablename__ = 'idc_asset_inventory_user_action_view'
    dgdh = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(50))
    department = db.Column(db.String(50))
    action_id = db.Column(db.Integer,primary_key=True)

class DepartmentView(db.Model):
    __tablename__ = 'idc_asset_inventory_department_view'
    department_id = db.Column(db.Integer,primary_key=True)
    department = db.Column(db.String(50))

class InventoryView(db.Model):
    __tablename__ = 'idc_asset_inventory_view'
    serial_no = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type_name = db.Column(db.String(20))
    idc_name = db.Column(db.String(20))
    cabinet = db.Column(db.String(20))
    cabinet_addresses = db.Column(db.Integer)
    host_name = db.Column(db.String(100))
    model = db.Column(db.String(50))
    asset_code = db.Column(db.String(20))
    asset_sn = db.Column(db.String(20))
    ip_business_code = db.Column(db.String(50))
    ip_value = db.Column(db.String(50))
    ip_admin = db.Column(db.String(50))
    department = db.Column(db.String(20))
    interfac_person = db.Column(db.String(10))
    project = db.Column(db.String(50))
    project_contract = db.Column(db.String(20))
    project_acceptance_time = db.Column(db.DATE)
    state = db.Column(db.Integer)
    off_shelf_evaluation = db.Column(db.Integer)
    cpu_config = db.Column(db.String(50))
    memory_config = db.Column(db.String(50))
    disk_config = db.Column(db.String(50))
    cpu_use_rate = db.Column(db.Integer)
    memory_use_rate = db.Column(db.Integer)
    disk_use_rate = db.Column(db.Integer)
    remark = db.Column(db.String(50))
    update_time = db.Column(db.TIMESTAMP, default=datetime.now, onupdate=datetime.now)
    is_delete = db.Column(db.Integer, default=0)







