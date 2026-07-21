# Python MySQL 操作复习

## 一、pymysql 原生操作

### 1.1 连接与建库

`pymysql.connect` 的核心参数：`host`、`port`、`user`、`password`、`database`、`charset`。建库场景下 `database` 参数不传，因为库还不存在——此时连接只完成 TCP + 鉴权，后续通过 `CREATE DATABASE` 语句建库。

```python
conn = pymysql.connect(host='localhost', port=3306,
                       user='root', password='123456', charset='utf8mb4')
cursor = conn.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS student_db CHARACTER SET utf8mb4")
```

关闭资源必须先 `cursor.close()` 再 `conn.close()`，否则可能导致连接泄露。

### 1.2 建表与增删改查

常用字段类型速查：

| 类型 | 对应 Python | 说明 |
|---|---|---|
| INT | int | 整数，常配合 AUTO_INCREMENT |
| VARCHAR(N) | str | 变长字符串，必须指定长度 |
| TINYINT | int/bool | 小整数，可用于布尔标记 |
| DECIMAL(M,D) | Decimal | 定点小数，适合金额/分数 |
| FLOAT | float | 浮点数 |
| DATETIME | datetime | 日期时间，常用 DEFAULT CURRENT_TIMESTAMP |

INSERT 单条：`VALUES (...)`；批量：`VALUES (...), (...), (...)`。UPDATE 和 DELETE 必须带 WHERE，否则全表生效。

**pymysql 默认不自动提交事务**，增删改后必须显式调用 `conn.commit()`，否则数据不会持久化。查询用 `cursor.fetchall()` 返回全部结果，`cursor.fetchone()` 返回一行。

```python
cursor.execute("INSERT INTO student(name, score) VALUES (%s, %s)", ("张三", 92.5))
conn.commit()
cursor.execute("SELECT * FROM student")
rows = cursor.fetchall()
```

### 1.3 工具类封装

封装目的：避免在每个操作中重复写 `connect` → `cursor` → `commit` → `close` 四步。

**参数化查询（防 SQL 注入）**：SQL 中用 `%s` 占位，实参以元组 `args` 传入 `cursor.execute(sql, args)`。pymysql 会自动转义，杜绝拼接字符串。

```python
class MySQLUtil:
    def __init__(self):
        self.conn = pymysql.connect(...)
        self.cursor = self.conn.cursor()

    def query_one(self, sql, args=None):
        self.cursor.execute(sql, args)
        return self.cursor.fetchone()

    def execute(self, sql, args=None):
        self.cursor.execute(sql, args or [])
        self.conn.commit()
        return self.cursor.rowcount  # 受影响行数
```

设计要点：`query_one` / `query_all` 只查不提交，`execute` 统一处理增删改并自动 commit。

---

## 二、SQLAlchemy 同步 ORM

### 2.1 三大组件与连接

SQLAlchemy 把 pymysql 的三步（conn + cursor + commit）抽象为三个对象：

| 组件 | 作用 | 对比 pymysql |
|---|---|---|
| `create_engine` | 数据库连接池引擎 | 替代 `pymysql.connect` |
| `declarative_base()` | 创建 ORM 模型基类 | 无对应（新概念） |
| `sessionmaker` → `db` | 会话工厂 → 会话对象 | 替代 cursor + commit |

连接串格式：`mysql+pymysql://user:pass@host:port/db?charset=utf8`。`echo=True` 可在控制台打印每条 SQL，调试时很有用。

```python
engine = create_engine('mysql+pymysql://root:123456@localhost:3306/test_db?charset=utf8')
Base = declarative_base()
db = sessionmaker(autocommit=False, autoflush=False, bind=engine)()
```

### 2.2 模型定义与建表

每个模型类继承 `Base`，类属性 → `Column(...)` 映射到表字段，`__tablename__` 指定真实表名。`Base.metadata.create_all(engine)` 一次性创建所有模型对应的表。

```python
class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    score = Column(Float, default=0.0)
    create_time = Column(DateTime, default=datetime.now)  # 注意：不加括号
```

**`default=datetime.now` 不加括号是常见坑**：传入的是函数对象本身，SQLAlchemy 每插入一行会调用它生成当前时间。写成 `datetime.now()` 会把模块加载时的固定时间写入所有行。

### 2.3 增删改查

核心范式：**查询即对象，改属性即修改，commit 即落盘**。

```python
# 增
db.add(obj)          # 单条
db.add_all([o1, o2]) # 批量
db.commit()

# 查
db.query(Class).all()                      # 全部
db.query(Class).filter(Class.id == 1).first()  # 单条
db.query(Class).filter(Class.score > 80).all() # 条件

# 改：查到对象 → 改属性 → commit
obj = db.query(Class).filter(...).first()
obj.score = 100
db.commit()

# 删
db.delete(obj)
db.commit()
```

**filter vs filter_by**：`filter` 支持比较运算符（`>`、`==`、`!=`）和 `or_`、`like`，功能更全面；`filter_by` 只支持等值条件，写法更简洁但局限。实战中优先用 `filter`。

排序：`order_by(-字段)` 倒序。分页：`offset(i).limit(n)`。模糊查询：`.filter(字段.like("%模式%"))`。聚合：`func.count()` / `func.avg()` / `func.sum()`，调用 `.scalar()` 取出单一数值。

### 2.4 事务回滚

事务保证一组操作要么全部持久化、要么全部不生效。当中间操作抛出异常，`rollback()` 将数据库状态回退到事务开始前。

```python
try:
    db.add(Class(class_name="python5班", teacher="杜甫", student_num=50))
    obj = db.query(Class).filter(Class.class_name == "python3班").first()
    obj.student_num = 30
    num = 1 / 0          # 模拟异常——新增和修改都不应生效
    db.commit()
except Exception:
    db.rollback()         # 回滚，两条变更全部撤销
```

适用场景：新增 + 修改等多步操作中途出错时，不应让部分数据生效。

---

## 三、SQLAlchemy 异步 ORM

### 3.1 异步引擎

异步 ORM 的关键差异：

| 对比项 | 同步 | 异步 |
|---|---|---|
| 引擎创建 | `create_engine` | `create_async_engine` |
| 驱动 | pymysql（同步 I/O） | aiomysql（异步 I/O） |
| 连接协议 | `mysql+pymysql://` | `mysql+aiomysql://` |
| 会话工厂 | `sessionmaker(bind=engine)` | `sessionmaker(engine, class_=AsyncSession)` |
| 建表 | `Base.metadata.create_all(engine)` | `await conn.run_sync(Base.metadata.create_all)` |
| CRUD | `db.query(...)` | `await db.execute(select(...))` |
| 关闭 | `engine.dispose()` | `await engine.dispose()` |

**engine.dispose() 必须显式调用**，否则 asyncio 事件循环关闭时可能抛出 "Event loop is closed" 错误。整个异步入口通过 `asyncio.run(main())` 启动。

```python
engine = create_async_engine("mysql+aiomysql://root:123456@localhost:3306/job_db?charset=utf8mb4")
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
```

### 3.2 同步 vs 异步性能对比

实验设计：同批 2000 条数据，分别用同步和异步引擎批量插入，`time.time()` 计时对比。异步在 I/O 密集场景下性能更优——数据库通信期间 CPU 不被阻塞，可调度其他协程。数据量小或网络延迟低时差异不明显，但并发量大时异步优势显著。

```python
# 同步
with SyncSession() as db:
    db.add_all(jobs)
    db.commit()

# 异步
async with AsyncSessionLocal() as db:
    db.add_all(jobs)
    await db.commit()
```

### 3.3 异步工具类封装

`AsyncJobManager` 完整封装了 `init_db` / `add` / `batch_add` / `query` / `query_page` / `update` / `delete` / `close` 八个方法，核心设计点：

- **条件查询动态拼接**：`select(JobPost)` 创建基础查询，用 `if` 判断参数，有值就 `.where()` 追加条件。
- **分页两步走**：先 `select(func.count())` 统计总数，再 `.limit().offset()` 取当前页数据，`offset = (page - 1) * page_size`。
- **更新用 setattr**：`setattr(job, key, value)` 动态修改属性，配合 `**kwargs` 实现灵活的字段更新。
- **ORM 对象转字典**：`to_dict()` 方法将 model 实例转为 dict，方便 JSON 序列化返回前端。

```python
async def query_page(self, page=1, page_size=10):
    async with self.async_session() as db:
        query = select(JobPost)
        total = (await db.execute(select(func.count()).select_from(query.subquery()))).scalar()
        query = query.limit(page_size).offset((page - 1) * page_size)
        jobs = (await db.execute(query)).scalars().all()
        return {"total": total, "page": page, "data": [j.to_dict() for j in jobs]}
```

---

## 四、综合实战

双模型系统（Student + ClassTable）覆盖了完整工作流：

- **批量新增**：`db.add_all()` 同时插入学生和班级数据，一次 commit 提交两张表。
- **综合查询**：排序 `order_by(-score)`、模糊 `like("张%")`、聚合 `func.avg().scalar()`。
- **修改删除**：查到对象 → 改属性 → commit；查最低分对象 → `db.delete()` → commit。

---

## 附录一：常见坑速查

1. **pymysql 忘记 commit**：增删改后数据未落盘，必须显式 `conn.commit()`。
2. **datetime.now 加了括号**：`default=datetime.now()` 会把模块加载时刻写入所有行，应去掉括号。
3. **UPDATE/DELETE 忘加 WHERE**：全表数据被修改或清空。
4. **%s 占位符写成 %d/%f**：pymysql 只用 `%s`，与 Python 字符串格式化无关。
5. **SQL 拼接导致注入**：用 `cursor.execute(sql, args)` 传参，绝不拼接字符串。
6. **异步 commit 忘加 await**：`db.commit()` 不会报错但数据未持久化，必须 `await db.commit()`。
7. **异步建表用同步方式**：必须 `await conn.run_sync(Base.metadata.create_all)`，不能直接调 create_all。
8. **忘记 engine.dispose()**：异步引擎不关闭会导致 "Event loop is closed" 错误。
9. **cursor 和 conn 关闭顺序反了**：先 cursor 后 conn。
10. **filter_by 用比较运算符**：`filter_by(score > 80)` 语法错误，必须改用 `filter(Class.score > 80)`。

---

## 附录二：API 速查表

### pymysql

| 操作 | 代码 |
|---|---|
| 连接 | `conn = pymysql.connect(host, port, user, password, database, charset)` |
| 游标 | `cursor = conn.cursor()` |
| 执行 | `cursor.execute(sql, args)` |
| 查一行 | `cursor.fetchone()` |
| 查全部 | `cursor.fetchall()` |
| 提交 | `conn.commit()` |
| 回滚 | `conn.rollback()` |
| 关闭 | `cursor.close()` → `conn.close()` |

### SQLAlchemy 同步

| 操作 | 代码 |
|---|---|
| 引擎 | `create_engine('mysql+pymysql://...')` |
| 基类 | `Base = declarative_base()` |
| 会话 | `db = sessionmaker(bind=engine)()` |
| 新增 | `db.add(obj)` / `db.add_all(list)` → `db.commit()` |
| 全查 | `db.query(Model).all()` |
| 条件查 | `db.query(Model).filter(...).first()` / `.all()` |
| 排序 | `.order_by(-字段)` |
| 分页 | `.offset(n).limit(m)` |
| 模糊 | `.filter(字段.like("%x%"))` |
| 聚合 | `func.count/avg/sum` + `.scalar()` |
| 修改 | 查对象 → 改属性 → `db.commit()` |
| 删除 | `db.delete(obj)` → `db.commit()` |
| 回滚 | `db.rollback()` |

### SQLAlchemy 异步

| 操作 | 代码 |
|---|---|
| 引擎 | `create_async_engine('mysql+aiomysql://...')` |
| 会话工厂 | `sessionmaker(engine, class_=AsyncSession)` |
| 建表 | `await conn.run_sync(Base.metadata.create_all)` |
| 查询 | `await db.execute(select(Model).where(...))` |
| 取结果 | `result.scalars().all()` / `.first()` |
| 新增 | `db.add(obj)` → `await db.commit()` → `await db.refresh(obj)` |
| 分页 | `select(func.count()).select_from(query.subquery())` 先计总数 |
| 更新 | `setattr(obj, key, val)` → `await db.commit()` |
| 删除 | `await db.delete(obj)` → `await db.commit()` |
| 关闭 | `await engine.dispose()` |
| 入口 | `asyncio.run(main())` |