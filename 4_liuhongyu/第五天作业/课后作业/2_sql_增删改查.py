import pymysql

conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='123456',
    database='student_db',
    charset = 'utf8mb4',
)

cursor = conn.cursor()

sql1 = """CREATE TABLE IF NOT EXISTS student (
    id INT PRIMARY KEY AUTO_INCREMENT COMMENT '主键自增ID',
    name VARCHAR(50) NOT NULL COMMENT '学生姓名',
    age TINYINT COMMENT '年龄',
    score DECIMAL(5,2) COMMENT '分数',
    create_time DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;"""

sql2 = "INSERT INTO student(name, age, score) VALUES ('张三', 18, 92.5);"

sql3 = """INSERT INTO student(name, age, score)
VALUES 
('李四', 19, 88),
('王五', 18, 95.5);"""

sql4 = "UPDATE student SET score=96 WHERE name='张三';"

sql5 = "DELETE FROM student WHERE id=3;"

sql6 = "SELECT * FROM student;"

cursor.execute(sql1)
print("表student创建成功")
cursor.execute(sql2)
print("插入数据成功")
cursor.execute(sql3)
print("批量插入数据成功")
cursor.execute(sql4)
print("更新数据成功")
cursor.execute(sql5)
print("删除数据成功")
cursor.execute(sql6)
print("查询数据成功")
conn.commit()
cursor.close()
conn.close()