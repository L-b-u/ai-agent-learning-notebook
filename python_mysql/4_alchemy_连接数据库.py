from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建数据库连接引擎
# 使用PyMySQL作为MySQL的驱动
# 连接参数说明：
# root: 数据库用户名
# 123456: 数据库密码
# localhost: 数据库主机地址
# 3306: 数据库端口号
# testdb: 要连接的数据库名
# charset=utf8: 设置字符编码为utf8
# echo=True: 显示SQL语句执行过程，便于调试
engine = create_engine('mysql+pymysql://root:123456@localhost:3306/test_db?charset=utf8',echo = True)

#创建基础模型类
Base = declarative_base()

#创建会话工厂
SessionLoc = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#创建会话
db = SessionLoc()

print("数据库连接成功")

db.execute("SELECT 1")
print("执行SQL语句成功")
db.close()