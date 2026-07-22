# Python HTTP 与爬虫基础复习

## 一、HTTP 协议核心

### 1.1 工作流程

HTTP 通信分为四步：建立 TCP 连接、发送 HTTP 请求、接收 HTTP 响应、关闭连接。`urllib.request.urlopen()` 一行代码封装了前三步。

```python
from urllib import request
url = "http://httpbin.org/get"
response = request.urlopen(url)
```

### 1.2 请求的组成

HTTP 请求由三部分构成：

- **请求行**：`GET /index.html HTTP/1.1` — 方法 + 资源路径 + 协议版本
- **请求头**：键值对形式的元信息（User-Agent、Host、Accept、Cookie、Referer、Content-Type 等）
- **请求体**：仅 POST / PUT / PATCH 携带，GET 请求无请求体

#### GET vs POST

| 维度 | GET | POST |
|---|---|---|
| 用途 | 获取数据（只读） | 提交数据（可修改） |
| 参数位置 | URL 查询字符串 `?key=value` | 请求体（Body） |
| 长度限制 | URL 最长约 2048 字符 | 理论上无限制 |
| 安全性 | 参数暴露在 URL 中 | 参数在请求体中，不暴露在 URL |
| 缓存 | 可被浏览器缓存 | 默认不缓存 |
| 幂等性 | 幂等（多次请求效果相同） | 不幂等（多次请求可能创建多条记录） |
| 典型场景 | 搜索、翻页、查看详情 | 登录、注册、表单提交 |

#### User-Agent 伪装

默认 Python 请求的 `User-Agent: Python-urllib/3.x` 极易被拒，需伪装成浏览器：

```python
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36"
}
```

注意：高级反爬仅伪装 User-Agent 不够，还会检查 Referer、Cookie 等其他头字段。

#### Cookie 的作用

Cookie 是维持登录状态的核心凭证。服务器通过 `Set-Cookie` 响应头下发，浏览器后续请求自动携带。爬虫模拟登录后，必须正确处理 Cookie 才能访问需登录态的页面。

#### 常见 Content-Type

| Content-Type | 场景 |
|---|---|
| `application/x-www-form-urlencoded` | 传统表单提交（`data` 参数） |
| `application/json` | 现代 API 调用（`json` 参数） |
| `multipart/form-data` | 文件上传 |

### 1.3 响应的组成

- **状态行**：`HTTP/1.1 200 OK` — 协议版本 + 状态码 + 状态描述
- **响应头**：Content-Type、Content-Length、Set-Cookie、Cache-Control 等
- **响应体**：HTML / JSON / 图片等实际内容

#### 状态码速记

| 范围 | 含义 | 速记 |
|---|---|---|
| 2xx | 成功 | 你要的东西给你了 |
| 3xx | 重定向 | 东西不在这，去别处找 |
| 4xx | 客户端错误 | 你的请求有问题 |
| 5xx | 服务器错误 | 服务器自己出问题了 |

爬虫中最棘手的两个状态码：

- **403 Forbidden** — 被反爬识别。对策：换 User-Agent、加 Cookie、降低频率、上代理 IP。
- **429 Too Many Requests** — 触发频率限制。对策：`time.sleep()` 延时、代理 IP 池轮换。

遇到 5xx 不要立即放弃，等待几秒重试可能恢复正常。

### 1.4 完整请求示例

```python
from urllib import request

url = "http://httpbin.org/get"
req = request.Request(url)
req.add_header("User-Agent",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)")

response = request.urlopen(req)

print("状态码:", response.status)
for key, value in response.headers.items():
    print(f"{key}: {value}")
print(response.read().decode("utf-8")[:200])
```

## 二、urllib 与 requests

### 2.1 urllib 基础（内置库）

```python
from urllib import request, parse

# 无参数 GET
response = request.urlopen("http://httpbin.org/get")
print(response.read().decode("utf-8"))

# 带参数 GET：parse.urlencode 将字典转为 URL 参数字符串
params = {"name": "张三", "age": 18}
url = "http://httpbin.org/get?" + parse.urlencode(params)
response = request.urlopen(url)
```

### 2.2 requests（第三方库，爬虫首选）

安装：`pip install requests`。相比 urllib 大幅简化代码量：

```python
# urllib（5 行）
from urllib import request
req = request.Request(url)
req.add_header("User-Agent", "Mozilla/5.0")
response = request.urlopen(req)
data = response.read().decode("utf-8")

# requests（2 行）
import requests
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
data = response.text
```

#### 常用方法

| 方法 | 用途 |
|---|---|
| `requests.get()` | 获取数据 |
| `requests.post()` | 提交数据 |
| `requests.put()` | 完整更新资源 |
| `requests.patch()` | 部分更新资源 |
| `requests.delete()` | 删除资源 |

#### 核心参数

- `url`：目标地址，必须以 `http://` 或 `https://` 开头
- `params`：URL 查询参数，接收字典，自动拼接到 URL 后面
- `headers`：请求头字典，爬虫伪装浏览器的关键
- `data`：POST 请求体，表单格式（`application/x-www-form-urlencoded`）
- `json`：POST 请求体，JSON 格式（`application/json`）
- `timeout`：超时秒数，爬虫必须设置防止卡死
- `cookies`：手动传递 Cookie 字典
- `proxies`：代理 IP 配置，格式 `{"http": "http://127.0.0.1:8080", "https": "https://127.0.0.1:8080"}`
- `allow_redirects`：是否跟随 3xx 重定向，默认 True。爬虫设 False 可拦截重定向链路。
- `verify`：SSL 证书验证，默认 True。自签名证书环境可设 False（不安全，仅限测试）。
- `stream`：流式下载开关。大文件下载时设 True，配合 `response.iter_content()` 分块写入，避免撑爆内存。

#### data vs json

```python
# 表单格式：适用于传统网页登录
response = requests.post(url, data={"username": "admin", "password": "123"})

# JSON 格式：适用于 API 调用
response = requests.post(url, json={"name": "小明", "age": 20})
```

#### 响应常用属性

| 属性 | 说明 |
|---|---|
| `response.status_code` | HTTP 状态码（int） |
| `response.text` | 文本内容（str，自动解码） |
| `response.content` | 二进制内容（bytes），图片/视频下载用这个 |
| `response.json()` | 直接解析 JSON 为 dict（前提 Content-Type 为 application/json） |
| `response.headers` | 响应头字典 |
| `response.encoding` | 编码方式，乱码时可手动修正：`response.encoding = "utf-8"` |
| `response.url` | 最终请求的 URL（经重定向后可能与原始 URL 不同） |

#### 代理与流式下载

代理通过 `proxies` 参数配置，将请求经中间服务器转发，隐藏真实 IP：

```python
proxies = {
    "http": "http://127.0.0.1:8080",
    "https": "https://127.0.0.1:8080"
}
response = requests.get(url, proxies=proxies, timeout=5)
```

大文件下载用 `stream=True` 分块写入，避免整个文件载入内存：

```python
response = requests.get(big_file_url, stream=True)
with open("large_file.zip", "wb") as f:
    for chunk in response.iter_content(chunk_size=8192):
        f.write(chunk)
```

### 2.3 Cookie 管理：手动 vs Session

**手动 cookies 参数**：每次请求单独传递，适合一次性场景。

```python
response = requests.get(url, cookies={"session": "abc123"})
```

**requests.Session()**：登录后自动缓存 Cookie，后续请求自动携带，完美模拟真人浏览。

```python
session = requests.Session()

# 服务器通过 Set-Cookie 下发 Cookie，Session 自动保存
session.get("http://httpbin.org/cookies/set/session_id/998877")

# 后续请求自动携带已保存的 Cookie
response1 = session.get("http://httpbin.org/get")  # 含 session_id=998877
response2 = session.get("http://httpbin.org/get")  # 依然携带
```

### 2.4 异常处理与超时

```python
import requests

try:
    response = requests.get(url, timeout=5)
    print(response.status_code)
except requests.exceptions.Timeout:
    print("请求超时")
except requests.exceptions.ConnectionError:
    print("连接失败")
except requests.exceptions.RequestException as e:
    print(f"其他错误：{e}")
```

批量请求场景中，`try-except` 是保证程序不中断的关键手段，统计成功/失败数以便事后分析：

```python
success = fail = 0
for url in url_list:
    try:
        resp = requests.get(url, timeout=15)
        if resp.status_code == 200:
            success += 1
        else:
            fail += 1
    except Exception:
        fail += 1
print(f"成功: {success}个 失败: {fail}个")
```

## 三、数据解析

### 3.1 JSON 解析

API 返回 JSON 字符串后，用 `json.loads()` 转为 Python 字典；反向用 `json.dumps()` 带 `ensure_ascii=False` 保留中文。

```python
import json

# JSON 字符串 -> 字典
data = json.loads('{"title": "Python工程师", "salary": "20-40K"}')
print(data["title"])

# 字典 -> JSON 字符串
json_str = json.dumps({"name": "张三", "age": 24}, ensure_ascii=False)
```

### 3.2 XPath 解析

安装 `lxml`：`pip install lxml`。核心流程：`etree.HTML()` 解析 HTML → 用 XPath 表达式定位元素 → 循环遍历提取子元素。

常用语法：

| 表达式 | 含义 |
|---|---|
| `//div` | 所有 div 元素 |
| `//div[@class="job"]` | class 为 job 的 div |
| `//h2/text()` | h2 标签的文本内容 |
| `//a/@href` | a 标签的 href 属性值 |
| `//ul/li[1]` | ul 下第一个 li |

典型提取流程：

```python
from lxml import etree

tree = etree.HTML(html_string)
jobs = tree.xpath('//div[@class="job"]')

for job in jobs:
    title = job.xpath('.//h2/text()')[0]    # 相对路径取子元素
    salary = job.xpath('.//p[@class="salary"]/text()')[0]
    city = job.xpath('.//p[@class="city"]/text()')[0]
    print(f"标题: {title}, 薪资: {salary}, 城市: {city}")
```

关键点：先用 `//div[@class='job']` 定位所有容器，再对每个容器用 `.//` 相对路径提取子元素，避免从根节点匹配导致数据错位。

## 四、综合实战：名言爬虫

一个完整爬虫项目包含四个模块：请求、解析、存储、交互控制。

**请求模块**：

```python
headers = {
    "User-Agent": "Mozilla/5.0 ... Chrome/150.0.0.0 Safari/537.36 Edg/150.0.0.0"
}
response = requests.get(url, headers=headers, timeout=5)
```

**解析模块** — lxml XPath 提取 content / author / tags：

```python
tree = etree.HTML(response.text)
for quote in tree.xpath('//div[@class="quote"]'):
    content = quote.xpath('.//span[@class="text"]/text()')[0]
    author = quote.xpath('.//small[@class="author"]/text()')[0]
    tags = quote.xpath('.//div[@class="tags"]/a/text()')
```

**存储模块** — SQLAlchemy ORM 存入数据库。模型定义三字段：`content`（名言文本）、`author`（作者）、`tags`（逗号拼接标签字符串）。每爬取一条就 `db.add()`，整页爬完后 `db.commit()` 一次性提交。

**交互控制** — `while` 循环命令行菜单，分步执行爬取（选择页数）和入库。异常发生时 `db.rollback()` 回滚，保证数据一致性。

**架构上的一条红线**：爬取和入库分步执行。爬取阶段只写入 SQLAlchemy 的 session 缓存不提交；用户确认后再 `commit` 写入磁盘。

## 附录：常见坑速查

1. **默认 User-Agent 被拒** — 必须伪装成浏览器 UA，否则目标站直接返回 403。
2. **拼写错误 `import request`** — 第三方库叫 `requests`（复数），`import request` 导入的是一个不存在的模块。
3. **中文 URL 编码问题** — 中文参数需 `parse.urlencode()` 编码，否则 URL 含非法字符请求失败。
4. **response.text 乱码** — 先用 `response.apparent_encoding` 推断编码，再手动设 `response.encoding = "utf-8"`。注意 `response.content` 是 bytes 不会乱码。
5. **XPath 索引从 1 开始** — `//li[1]` 取第一个，与 Python 的 0-based 索引相反，极易搞混。
6. **XPath 不加点号导致全局匹配** — 遍历容器内子元素必须用 `.//`，直接用 `//` 会从文档根节点全局搜索，导致所有容器取到相同数据。
7. **XPath 取 text() 返回列表** — `xpath('.//h2/text()')` 返回的是列表，即使只有一个元素也要加 `[0]`，否则直接拼接字符串时报错。
8. **XPath 属性值加引号** — `[@class="job"]` 中属性值必须用引号括起来，写成 `[@class=job]` 会语法错误。
9. **Session 忘记复用** — 每次 `requests.get()` 不带 Session 则无法保持登录态，鉴权后的页面访问失败。
10. **忘记设置 timeout** — 爬虫无超时设置可能永久阻塞，生产环境必须加。timeout 的单位是秒。
11. **POST 用错 data / json** — 调 API 用 `json=` 参数（自动设 Content-Type: application/json），传统表单才用 `data=`（application/x-www-form-urlencoded）。
12. **json.dumps 中文变 \uXXXX** — 不加 `ensure_ascii=False`，中文会被转义为 Unicode 码点，存入文件不可读。
13. **异常捕获范围过大** — 整页爬取失败 `rollback` 后继续处理下一页，不应终止整个程序。
14. **db.commit() 前忘记 db.add()** — SQLAlchemy ORM 先 add 到 session 缓存，commit 才真正写入数据库。顺序不可反。
15. **引擎 echo=True 在生产环境** — 会把所有 SQL 打印到控制台，正式上线前务必关掉或改为 False。
16. **爬取频率过高被封 IP** — 加入 `time.sleep(1~5)` 随机延时 + 代理 IP 池轮换，降低被封概率。
17. **重定向后 URL 变化未察觉** — `response.url` 可查看最终落点 URL，用于判断是否被反爬跳转到验证页。
