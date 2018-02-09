from sqlalchemy import create_engine, func
from sqlalchemy import alias, and_, func,outerjoin, or_
from sqlalchemy.orm import sessionmaker, aliased
from app.models import *
engine=create_engine("mysql+pymysql://11q:jczc@666@172.25.135.121:3306/wasu?charset=utf8", encoding='utf8')

class ConnectionPool():
    def __init__(self):
        self.session = None

    def __enter__(self):
        DBSession = sessionmaker(bind=engine)
        self.session = DBSession()
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()


def list_data(**kwargs):
    page = kwargs.get('page', 1)
    row_count = kwargs.get('row_count', 15)
    with ConnectionPool() as session:
        data = session.query(InventoryView).group_by(InventoryView.serial_no).offset(page).limit(row_count).all()
        count = session.query(InventoryView).filter(InventoryView.is_delete == 0).count()
    return data, count

def list_search(word,**kwargs):
    page = kwargs.get('page',1)
    row_count = kwargs.get('row_count',15)
    with ConnectionPool() as session:
        data = session.query(InventoryView).group_by(InventoryView.serial_no).filter(or_(    InventoryView.type_name.contains(word),InventoryView.idc_name.contains(word),InventoryView.cabinet.contains(word),InventoryView.model.contains(word),InventoryView.department.contains(word),InventoryView.interfac_person.contains(word))).offset(page).limit(row_count).all()
        count = session.query(InventoryView).filter(InventoryView.is_delete == 0).count()
    return data,count

def get_user(user_id):
    with ConnectionPool() as session:
        data = session.query(User).filter_by(dgdh=user_id
        ).first()
    return data if data else None

def insert_inventory(**kwargs):
    with ConnectionPool() as session:
        ine = Inventory(**kwargs)
        session.add(ine)
        session.commit()

def insert_inventory_ip(**kwargs):
    with ConnectionPool() as session:
        ip = Inventory_Ip(**kwargs)
        session.add(ip)
        session.commit()

def list_department():
    with ConnectionPool() as session:
        data = session.query(DepartmentView).all()
    return data


def delete_inventory(serial_nos):
    with ConnectionPool() as session:
        inv = session.query(Inventory).filter(Inventory.serial_no.in_(serial_nos)).all()
        session.delete(inv)
        session.commit()

def delete_inventory_ip(serial_nos):
    with ConnectionPool() as session:
        inv_ip = session.query(Inventory_Ip).filter(and_(Inventory.serial_no.in_(serial_nos),Inventory.ip_business_code == Inventory_Ip.ip_business_code)).all()
        session.delete(inv_ip)
        session.commit()

def get_inventory(serial_no):
    with ConnectionPool() as session:
        data = session.query().filter().one()
    return data

def add_regiest(worknum,username,password):
    with ConnectionPool() as session:
        user = User(dgdh=worknum,name=username,password=password)
        session.add(user)
        session.commit()

def get_worknum(worknum):
    with ConnectionPool() as session:
        work = session.query(User).filter_by(dgdh = worknum ).first()
    return work

def login(username,password):
    with ConnectionPool() as session:
        data = session.query(User).filter_by(name = username).first()
        if data and data.verify_password(password):
            return data

