from sqlalchemy import create_engine, Column, Integer, String,Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from datetime import datetime
# 1. 数据库连接
engine = create_engine('mysql+pymysql://root:123456@localhost:3306/test_db?charset=utf8')
Base = declarative_base()
SessionLoc = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = SessionLoc()
# 2. 模型定义
class Student(Base):
    __tablename__ = "student_table2"
    id = Column(Integer, primary_key=True, autoincrement=True, comment='主键')
    name = Column(String(20), nullable=False, comment='姓名')
    age = Column(Integer, nullable=False,default=18,comment='年龄')
    gender = Column(String(10), default="未知",comment='性别')
    score = Column(Float, default=0.0,comment='成绩')
    create_time = Column(DateTime, default=datetime.now,comment='创建时间')

class ClassTable(Base):
    __tablename__ = 'class_table2'
    id = Column(Integer, primary_key=True, autoincrement=True, comment='主键')
    class_name = Column(String(20), nullable=False, unique=True, comment='班级名称')
    teacher = Column(String(20), nullable=False, comment='班主任')
    student_num = Column(Integer, default=0, comment='班级人数')

# 3. 创建表

Base.metadata.create_all(engine)
print("表创建成功")

# 4. 批量新增数据
def add_test_data():
    stu1 = Student(id = 2001, name = "张三", age = 19, gender = "男", score = 95)
    stu2 = Student(id = 2002, name = "李四", age = 18, gender = "男", score = 85)
    stu3 = Student(id = 2003, name = "王五", age = 19, gender = "男", score = 75)
    stu4 = Student(id = 2004, name = "赵六", age = 18, gender = "男", score = 99)
    cls1 = ClassTable(id=1, class_name="python1班", teacher="王老师", student_num=25)
    cls2 = ClassTable(id=2,class_name="python2班",teacher="季老师",student_num=20)
    cls3 = ClassTable(id=3,class_name="python3班",teacher="雷老师",student_num=35)
    stu_list = [stu1,stu2,stu3,stu4]
    cls_list = [cls1, cls2, cls3]
    db.add_all(stu_list)
    db.add_all(cls_list)
    db.commit()
    print("学生表和班级表添加数据成功")

# 5. 综合查询
def query_all_data():
    # 高分学生排序
    sort_score = db.query(Student).order_by(-Student.score).all()
    print("高分学生排序为:")
    for i in sort_score:
        print(i.name,i.score)

    # 模糊查询 查找并统计姓张的同学数量
    zhang_stu = db.query(Student).filter(Student.name.like("张%")).all()
    zhang_count = db.query(Student).filter(Student.name.like("%张%")).all()
    print("姓张的学生：")
    for s in zhang_stu:
        print(s.name)
    print(f"姓张同学总数量：{len(zhang_count)}")
     # 统计 所有学生的平均分
    score_avg = db.query(func.avg(Student.score)).scalar()
    print("所有学生的平均分为:",score_avg)

# 6. 修改删除
def update_del_data():
    # 修改数据：修改id为2001的同学的成绩为100.0
    u = db.query(Student).filter(Student.id==2001).first()
    if u:
        u.score = 100
        db.commit()
        print("修改学生的成绩成功")
    else:
        print("没有找到该学生")
    # 删除数据：删除成绩最低的学生数据
    min_score_stu = db.query(Student).order_by(Student.score).first()
    if min_score_stu:
        db.delete(min_score_stu)
        db.commit()
        print(f"删除成绩最低学生：{min_score_stu.name},分数：{min_score_stu.score}")
    else:
        print("无学生数据可删除")

# 执行所有功能
if __name__ == "__main__":
    # add_test_data()
    query_all_data()
    update_del_data()
    db.close()