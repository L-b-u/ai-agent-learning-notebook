from urllib import request

#1. 建立连接 + 发送请求
url = "http://httpbin.org/get"
response = request.urlopen(url)

#接收响应
print("状态码:", response.status)
print("响应头:", response.headers)
print("响应内容:", response.read().decode("utf-8"))