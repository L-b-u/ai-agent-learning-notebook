#封装通用工具

import pymysql

class MYSQLUtil:
    def __init__(self):
        self.conn = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='123456',
            database='student_db',
            charset='utf8mb4',
        )
        self.cursor = self.conn.cursor()
    #查询
    def query_one(self, sql, args=None):
        self.cursor.execute(sql, args)
        return self.cursor.fetchone()
    def query_all(self, sql, args=None):
        self.cursor.execute(sql, args)
        return self.cursor.fetchall()

    #增删改
    def execute(self, sql, args=None):
        self.cursor.execute(sql, args or [])
        self.conn.commit()
        return self.cursor.rowcount

    #关闭连接
    def close(self):
        self.cursor.close()
        self.conn.close()

if __name__ == "__main__":
    db = MYSQLUtil()
    #1.查询
    sql = "SELECT * FROM student;"
    result = db.query_all(sql)
    print("查询结果：", result)

    #2.增删改
    sql = "INSERT INTO student(name, age, score) VALUES (%s, %s, %s);"
    args = ("李四", 19, 88.5)
    rowcount = db.execute(sql, args)
    print("受影响的行数：", rowcount)

    #关闭
    db.close()