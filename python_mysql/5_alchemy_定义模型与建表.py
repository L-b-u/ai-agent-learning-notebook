from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime


engine = create_engine('mysql+pymysql://root:123456@localhost:3306/test_db?charset=utf8',echo = True)

Base = declarative_base()
SessionLoc = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = SessionLoc()

#用类的方式定义
# class Student(Base):
#     __tablename__ = 'student'#数据中实际的表名
#     id = Column(Integer, primary_key=True, autoincrement=True,comment='主键')
#     name = Column(String(20), nullable=False, comment='姓名')
#     age = Column(Integer, nullable=False,default=18,comment='年龄')
#     gender = Column(String(10), default="未知",comment='性别')
#     score = Column(Float, default=0.0,comment='成绩')
#     create_time = Column(DateTime, default=datetime.now,comment='创建时间')

class Class(Base):
    __tablename__ = 'class_table'
    id = Column(Integer, primary_key=True, autoincrement=True,comment='主键')
    class_name = Column(String(20), nullable=False,unique=True,comment='班级名称')
    teacher = Column(String(20), nullable=False,comment='班主任')
    student_num = Column(Integer, default=0,comment='班级人数')

#创建数据表
Base.metadata.create_all(engine)
print("创建成功")

if __name__ == '__main__':
    try:
        Base = Base.metadata.create_all(engine)
        print("数据表创建成功")
    except Exception as e:
        print("数据表创建失败",e)
