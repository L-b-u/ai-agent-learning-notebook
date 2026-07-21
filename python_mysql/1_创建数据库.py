import pymysql

conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='123456',
    charset = 'utf8mb4',
)

cursor = conn.cursor()

sql1 = "CREATE DATABASE IF NOT EXISTS test_db CHARACTER SET utf8mb4 ;"
sql2 = "CREATE DATABASE IF NOT EXISTS student_db CHARACTER SET utf8mb4 ;"

cursor.execute(sql1)
print("数据库test_db创建成功")
cursor.execute(sql2)
print("数据库student_db创建成功")

cursor.close()
conn.close()