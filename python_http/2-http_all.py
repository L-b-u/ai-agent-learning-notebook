from urllib import request

url = "http://httpbin.org/get"

#创建一个请求对象
req = request.Request(url)
req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64)")

#发送请求
response = request.urlopen(req)

#查看完成响应
print("===状态码===")
print(response.status)

print("\n===响应头===")
print(type(response.headers))
for key, value in response.headers.items():
    print(f"{key}: {value}")

print("\n===响应内容===")
print(response.read().decode("utf-8")[:200])