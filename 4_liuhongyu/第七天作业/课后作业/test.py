"""
政府网头条新闻爬虫
技术栈：requests + BeautifulSoup4 + html.parser + SQLAlchemy + SQLite
目标网址：https://www.gov.cn/toutiao/liebiao/
抓取范围：第1~10页
"""
import time
import random
import requests
from bs4 import BeautifulSoup
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# ============================================================
# 一、数据库模型
# ============================================================
Base = declarative_base()


class GovNews(Base):
    __tablename__ = "gov_news"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(500), nullable=False)
    publish_time = Column(String(30), nullable=False)
    link = Column(String(800), unique=True, nullable=False)


# ============================================================
# 二、爬虫工具类
# ============================================================
class GovSpider:
    def __init__(self):
        self.engine = create_engine("sqlite:///gov_news.db", echo=False)
        Base.metadata.create_all(bind=self.engine)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        self.db = self.SessionLocal()

        self.headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/150.0.0.0 Safari/537.36 Edg/150.0.0.0"
            ),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Referer": "https://www.gov.cn/",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
        }

    def crawl_page(self, page_num):
        """抓取单页，数据 add 进会话缓存"""
        if page_num == 1:
            url = "https://www.gov.cn/toutiao/liebiao/"
        else:
            url = f"https://www.gov.cn/toutiao/liebiao/home_{page_num - 1}.htm"

        try:
            resp = requests.get(url, headers=self.headers, timeout=5)
            print(f"第{page_num}页 状态码: {resp.status_code}")

            if resp.status_code == 403:
                print(f"[终止] 第{page_num}页返回403，触发反爬")
                return "blocked"

            resp.encoding = "utf-8"

            # 必须用 html.parser！lxml 解析器与该页面 HTML 不兼容
            soup = BeautifulSoup(resp.text, "html.parser")

            # CSS 选择器定位每条新闻
            news_items = soup.select("div.news_box ul li")
            if not news_items:
                news_items = soup.select("div.list ul li")

            if not news_items:
                print(f"[警告] 第{page_num}页未找到新闻条目")
                return True

            count = 0
            for item in news_items:
                try:
                    a_tag = item.select_one("h4 a")
                    if not a_tag:
                        continue

                    title = a_tag.get_text(strip=True)
                    href = a_tag.get("href", "")
                    full_link = href if href.startswith("http") else "https://www.gov.cn" + href

                    date_tag = item.select_one("h4 span.date")
                    pub_time = date_tag.get_text(strip=True) if date_tag else ""

                    if not title or not pub_time:
                        continue

                    self.db.add(GovNews(title=title, publish_time=pub_time, link=full_link))
                    count += 1

                except Exception as e:
                    print(f"[警告] 第{page_num}页单条解析异常: {e}")
                    continue

            print(f"[完成] 第{page_num}页解析 {count} 条，已缓存")
            return True

        except requests.exceptions.Timeout:
            print(f"[异常] 第{page_num}页请求超时")
            return True
        except requests.exceptions.ConnectionError:
            print(f"[异常] 第{page_num}页连接失败")
            return True
        except requests.exceptions.RequestException as e:
            print(f"[异常] 第{page_num}页网络错误: {e}")
            return True
        except Exception as e:
            print(f"[异常] 第{page_num}页解析失败: {e}")
            return True

    def save_db(self):
        try:
            self.db.commit()
            print("数据入库成功")
        except Exception as e:
            self.db.rollback()
            print(f"入库失败，已回滚: {e}")

    def close(self):
        self.db.close()


# ============================================================
# 三、主程序
# ============================================================
def main():
    spider = GovSpider()

    while True:
        print("\n==== 政府网头条新闻爬虫 ====")
        print("1. 指定单页抓取（缓存，不提交）")
        print("2. 批量抓取第1~10页（自动入库）")
        print("3. 提交缓存数据到数据库")
        print("4. 退出")
        try:
            choice = int(input("请输入选项: "))
        except ValueError:
            print("请输入数字")
            continue

        if choice == 1:
            try:
                page = int(input("页码: "))
            except ValueError:
                print("请输入数字")
                continue
            spider.crawl_page(page)

        elif choice == 2:
            print("开始抓取第1~10页...")
            for page in range(1, 11):
                result = spider.crawl_page(page)
                if result == "blocked":
                    break
                delay = random.uniform(2, 4)
                print(f"[休眠] {delay:.1f} 秒\n")
                time.sleep(delay)
            spider.save_db()
            print("批量抓取完成")

        elif choice == 3:
            spider.save_db()

        elif choice == 4:
            spider.close()
            print("已退出")
            break

        else:
            print("无效选项")


if __name__ == "__main__":
    main()
