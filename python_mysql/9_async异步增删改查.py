"""
异步 CRUD 完整实战
增删改查、分页查询、条件过滤、工具类封装
"""
import asyncio
from datetime import datetime
from typing import List, Dict, Any, Optional

from sqlalchemy import Column, Integer, String, Float, DateTime, Text, select, func
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

# ========== 初始化 ==========
# engine 在下方 AsyncJobManager.__init__ 中通过参数传入，避免重复创建连接池
Base = declarative_base()
engine = create_async_engine(
        "mysql+aiomysql://root:123456@localhost:3306/job_db?charset=utf8mb4",
        echo=False
    )

class JobPost(Base):
    __tablename__ = "job_post"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    company = Column(String(100), nullable=False)
    salary_min = Column(Float, default=0)
    salary_max = Column(Float, default=0)
    experience = Column(String(50), default="不限")
    jd_text = Column(Text)
    create_time = Column(DateTime, default=datetime.now)

    def __repr__(self):
        return f"<{self.title} @ {self.company} {self.salary_min}-{self.salary_max}k>"

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "company": self.company,
            "salary_min": self.salary_min,
            "salary_max": self.salary_max,
            "experience": self.experience,
            "create_time": str(self.create_time) if self.create_time else None
        }


# ========== 工具类 ==========
class AsyncJobManager:
    """异步岗位管理工具类"""

    def __init__(self, engine):
        self.engine = engine
        self.async_session = sessionmaker(
            self.engine, class_=AsyncSession, expire_on_commit=False
        )

    async def init_db(self):
        """初始化数据表"""
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        print("数据表初始化完成")

    async def add_job(self, title: str, company: str, salary_min: float,
                      salary_max: float, experience: str, jd_text: str) -> int:
        """添加岗位"""
        async with self.async_session() as db:
            job = JobPost(
                title=title, company=company,
                salary_min=salary_min, salary_max=salary_max,
                experience=experience, jd_text=jd_text
            )
            db.add(job)
            await db.commit()
            await db.refresh(job)
            print(f"添加成功: {job.title}")
            return job.id

    async def batch_add(self, jobs_data: List[Dict]) -> int:
        """批量添加"""
        async with self.async_session() as db:
            jobs = [JobPost(**data) for data in jobs_data]
            db.add_all(jobs)
            await db.commit()
            print(f"批量添加成功: {len(jobs)} 条")
            return len(jobs)

    async def query(self, salary_min: Optional[float] = None,
                    experience: Optional[str] = None) -> List[Dict]:
        """条件查询"""
        async with self.async_session() as db:
            query = select(JobPost)
            if salary_min is not None:
                query = query.where(JobPost.salary_min >= salary_min)
            if experience is not None:
                query = query.where(JobPost.experience == experience)

            result = await db.execute(query)
            jobs = result.scalars().all()
            return [job.to_dict() for job in jobs]

    async def query_page(self, page: int = 1, page_size: int = 10,
                         salary_min: Optional[float] = None) -> Dict:
        """分页查询"""
        async with self.async_session() as db:
            query = select(JobPost)
            if salary_min is not None:
                query = query.where(JobPost.salary_min >= salary_min)

            # 总数
            count_query = select(func.count()).select_from(query.subquery())
            total_result = await db.execute(count_query)
            total = total_result.scalar()

            # 分页
            query = query.limit(page_size).offset((page - 1) * page_size)
            result = await db.execute(query)
            jobs = result.scalars().all()

            return {
                "total": total,
                "page": page,
                "page_size": page_size,
                "data": [job.to_dict() for job in jobs]
            }

    async def update_job(self, job_id: int, **kwargs) -> bool:
        """更新岗位"""
        async with self.async_session() as db:
            result = await db.execute(
                select(JobPost).where(JobPost.id == job_id)
            )
            job = result.scalars().first()
            if job:
                for key, value in kwargs.items():
                    if hasattr(job, key):
                        setattr(job, key, value)
                await db.commit()
                await db.refresh(job)
                print(f"更新成功: {job.title}")
                return True
            return False

    async def delete_job(self, job_id: int) -> bool:
        """删除岗位"""
        async with self.async_session() as db:
            result = await db.execute(
                select(JobPost).where(JobPost.id == job_id)
            )
            job = result.scalars().first()
            if job:
                await db.delete(job)
                await db.commit()
                print(f"删除成功: {job.title}")
                return True
            return False

    async def close(self):
        """关闭连接"""
        await self.engine.dispose()


# ========== 主函数 ==========
async def main():

    manager = AsyncJobManager(engine)
    await manager.init_db()

    print("=" * 60)
    print("异步 CRUD 完整实战")
    print("=" * 60)

    # 1. 批量添加
    print("\n【1. 批量添加】")
    jobs_data = [
        {"title": "Python后端开发", "company": "字节跳动", "salary_min": 18, "salary_max": 35,
         "experience": "3-5年", "jd_text": "负责后端服务开发..."},
        {"title": "Java架构师", "company": "阿里巴巴", "salary_min": 30, "salary_max": 60,
         "experience": "5年以上", "jd_text": "负责核心系统架构..."},
        {"title": "前端工程师", "company": "腾讯", "salary_min": 15, "salary_max": 30,
         "experience": "1-3年", "jd_text": "负责Web端产品开发..."},
        {"title": "算法工程师", "company": "百度", "salary_min": 25, "salary_max": 50,
         "experience": "3-5年", "jd_text": "负责NLP算法研发..."},
        {"title": "测试开发", "company": "美团", "salary_min": 12, "salary_max": 22,
         "experience": "不限", "jd_text": "负责自动化测试..."}
    ]
    await manager.batch_add(jobs_data)

    # 2. 条件查询
    print("\n【2. 条件查询：薪资>=20k】")
    results = await manager.query(salary_min=20)
    print(f"查询结果: {len(results)} 条")
    for r in results:
        print(f"  {r['title']} @ {r['company']}")

    # 3. 分页查询
    print("\n【3. 分页查询：第1页，每页2条】")
    page_result = await manager.query_page(page=1, page_size=2)
    print(f"总数: {page_result['total']}, 当前页: {page_result['page']}")
    for r in page_result['data']:
        print(f"  {r['title']} @ {r['company']}")

    # 4. 更新
    print("\n【4. 更新岗位】")
    if results:
        job_id = results[0]['id']
        await manager.update_job(job_id, salary_min=25, salary_max=40)

    # 5. 删除
    print("\n【5. 删除岗位】")
    if results:
        job_id = results[-1]['id']
        await manager.delete_job(job_id)

    # 6. 最终查询
    print("\n【6. 最终数据】")
    final_results = await manager.query()
    print(f"剩余: {len(final_results)} 条")
    for r in final_results:
        print(f"  {r['title']} @ {r['company']}")

    await manager.close()


if __name__ == "__main__":
    asyncio.run(main())
