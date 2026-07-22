"""
任务：
1.http://quotes.toscrape.com/爬取 名言内容，作者，标签
2.try-exception 异常捕获
3.状态码，response.text
4.请求头，浏览器里面找，timeout=5s
5.SQLAlchemy存入MySQL
6.控制界面
结构：工具类只提供方法，main实现交互逻辑
"""
import requests
from lxml import etree
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# ---------------------- ORM 数据表模型 ----------------------
Base = declarative_base()
class Test(Base):
    __tablename__ = "test"
    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(Text, nullable=False)    # 名言
    author = Column(String(100), nullable=False)  # 作者
    tags = Column(String(300))                # 标签，逗号拼接

# 工具类
class SpiderTool:
    def __init__(self):
        # 数据库连接
        self.engine = create_engine("mysql+pymysql://root:123456@127.0.0.1:3306/quote_db", echo=True)
        Base.metadata.create_all(bind=self.engine)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        self.db = self.SessionLocal()

        # 请求头
        self.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "accept-encoding": "gzip, deflate",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Host": "quotes.toscrape.com",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36 Edg/150.0.0.0"
        }

    def crawl(self, page):
        """工具方法：爬取指定页码，数据add进会话缓存"""
        try:
            if page == 1:
                url = "http://quotes.toscrape.com/"
            else:
                url = f"http://quotes.toscrape.com/page/{page}/"

            response = requests.get(url, headers=self.headers, timeout=5)
            print(f"状态码：{response.status_code}")
            html = response.text
            tree = etree.HTML(html)
            quotes = tree.xpath('//div[@class="quote"]')

            for quote in quotes:
                content = quote.xpath('.//span[@class="text"]/text()')[0]
                author = quote.xpath('.//small[@class="author"]/text()')[0]
                tag_list = quote.xpath('.//div[@class="tags"]/a/text()')
                tags_str = ",".join(tag_list)

                print(f"爬取到的名言内容: {content}")
                print(f"爬取到的作者: {author}")
                print(f"爬取到的标签: {tag_list}")
                print("-" * 40)

                item = Test(content=content, author=author, tags=tags_str)
                self.db.add(item)
            print("当前页面数据已加载缓存")

        except requests.exceptions.Timeout:
            print("请求超时，换个网址试试")
            self.db.rollback()
        except requests.exceptions.ConnectionError:
            print("连接失败，检查网络")
            self.db.rollback()
        except requests.exceptions.RequestException as e:
            print(f"其他网络错误：{e}")
            self.db.rollback()
        except Exception as e:
            print(f"解析异常：{e}")
            self.db.rollback()

    def save_db(self):
        """工具方法：提交缓存数据存入数据库"""
        try:
            self.db.commit()
            print("所有数据录入成功！")
        except Exception as e:
            self.db.rollback()
            print(f"入库失败：{e}")

    def close(self):
        """工具方法：关闭数据库会话"""
        self.db.close()

# ---------------------- main函数：实现交互业务逻辑 ----------------------
def main():
    # 实例化工具类
    tool = SpiderTool()
    while True:
        print("\n====欢迎来到名言爬虫系统====")
        print("输入1开始爬取（输入页码）")
        print("输入2将缓存数据存入数据库")
        print("输入3退出程序")
        try:
            choice = int(input("请输入你的选择："))
        except ValueError:
            print("请输入数字！")
            continue

        if choice == 1:
            page = int(input("请输入爬取的页数："))
            tool.crawl(page)
        elif choice == 2:
            tool.save_db()
        elif choice == 3:
            print("退出成功")
            tool.close()
            break
        else:
            print("输入选项无效，请重新选择！")

if __name__ == "__main__":
    main()