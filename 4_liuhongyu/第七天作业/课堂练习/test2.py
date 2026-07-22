"""
课堂任务：
1.http://quotes.toscrape.com/爬取 名言内容，作者，标签
2.try-excption 异常捕获
3.状态码，response.text
4.请求头，浏览器里面找，，timeout=5s
5.alchemy存在sqlite
6.控制界面
"""
import requests
from lxml import etree
from sqlalchemy import create_engine, Column, Integer, String,Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# engine = create_engine("sqlite:///test.db", echo=True)
engine = create_engine("mysql+pymysql://root:123456@127.0.0.1:3306/quote_db", echo=True)
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Test(Base):
    __tablename__ = "test"
    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(Text, nullable=False)  # 名言
    author = Column(String(100), nullable=False)  # 作者
    tags = Column(String(300))  # 标签，逗号拼接保存

Base.metadata.create_all(bind=engine)
db = SessionLocal()


headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": "gzip, deflate",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Host": "quotes.toscrape.com",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36 Edg/150.0.0.0"
}

def main(num,page = 1):
    try:
        if num == 1:
            if page == 1:
                url = "http://quotes.toscrape.com/"
            else:
                url = f"http://quotes.toscrape.com/page/{page}/"
            response = requests.get(url, headers=headers, timeout=5)
            print(f"状态码：{response.status_code}")
            html = response.text
            tree = etree.HTML(html)
            quotes = tree.xpath('//div[@class="quote"]')
            for quote in quotes:
                content = quote.xpath('.//span[@class="text"]/text()')[0]
                print(f"爬取到的名言内容: {content}")
                author = quote.xpath('.//small[@class="author"]/text()')[0]
                print(f"爬取到的作者: {author}")
                tags = quote.xpath('.//div[@class="tags"]/a/text()')
                print(f"爬取到的标签: {tags}")

                test = Test(content=content, author=author, tags=",".join(tags))
                db.add(test)
            print("查询数据完成")
        if num == 2:
            db.commit()
            print("所有数据录入成功")
    except requests.exceptions.Timeout:
            print("请求超时，换个网址试试")
            db.rollback()
    except requests.exceptions.ConnectionError:
            print("连接失败，检查网络")
            db.rollback()
    except requests.exceptions.RequestException as e:
            print(f"其他错误：{e}")
            db.rollback()

if __name__ == "__main__":
    while True:
        print("欢迎来到名言爬虫系统")
        print("输入1开始爬取")
        print("输入2添加到数据库")
        print("输入3退出")
        choice = int(input("请输入你的选择："))
        if choice == 1:
            page = int(input("请输入爬取的页数："))
            main(choice,page)
        elif choice == 2:
            main(choice)
        else:
            print("退出成功")
            db.close()
            break





