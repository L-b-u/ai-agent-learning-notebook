from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from datetime import datetime

engine = create_engine('mysql+pymysql://root:123456@localhost:3306/test_db?charset=utf8')

Base = declarative_base()
SessionLoc = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = SessionLoc()

#用类的方式定义
# class Student(Base):
#     __tablename__ = 'student'#数据中实际的表名
#     id = Column(Integer, primary_key=True, autoincrement=True,comment='主键')
#     name = Column(String(20), nullable=False,default=18, comment='姓名')
#     age = Column(Integer, nullable=False,comment='年龄')
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

# cls1 = Class(id=1,class_name="python1班",teacher="张三",student_num=10)
# cls2 = Class(id=2,class_name="python2班",teacher="李四",student_num=20)
# cls3 = Class(id=3,class_name="python3班",teacher="王五",student_num=30)
# db.add_all([cls1,cls2,cls3])
# db.commit()
# print("班级数据添加成功")
#查询所有班级数据
# all_class = db.query(Class).all()
# for i in all_class:
#     print(i.id, i.class_name, i.teacher, i.student_num)
# #查询主键为1的班级
# cls = db.query(Class).filter(Class.id==1).first()
# print(cls.id, cls.class_name, cls.teacher, cls.student_num)
#
# cls_num = db.query(Class).filter(Class.student_num>0).all()
# for item in cls_num:
#     print(item.class_name, item.teacher)

# u = db.query(Class).filter(Class.class_name=="python3班").first()
# if u:
#     u.teacher = "赵六"
#     u.student_num = 40
#     db.commit()
#     print("修改班主任和学生人数成功")
# else:
#     print("没有找到该班级")

# try:
#     cls4 = Class(id=4, class_name="python5班",teacher="杜甫",student_num=50)
#     db.add(cls4)
#     u = db.query(Class).filter(Class.class_name=="python3班").first()
#     if u:
#         u.student_num = 30
#         num = 1 / 0
#         db.commit()
#         print("修改成功")
#     else:
#         print("没有找到该班级")
# except Exception as e:
#     db.rollback()
#     print("进行回滚")
# finally:
#     db.close()
#对班级人数进行倒序排序
# sort_stu = db.query(Class).order_by(-Class.student_num).all()
# for item in sort_stu:
#     print(item.class_name, item.teacher, item.student_num)

#分页查询：第1页，每页1条数据
# page = db.query(Class).offset(0).limit(1).all()
# for item in page:
#     print(item.class_name, item.teacher, item.student_num)

#模糊查询班级名包含“Python”的班级
# res = db.query(Class).filter(Class.class_name.like("%python%")).all()
# for item in res:
#     print(item.class_name)

#统计班级总数量、总人数平均值
# count = db.query(func.count(Class.id)).scalar()
# print(count)
# count_avg = db.query(func.avg(Class.student_num)).scalar()
# print(count_avg)


