from asyncio import timeout
import requests

url_list = ["http://httpbin.org/get", "http://httpbin.org/status/200", "http://httpbin.org/status/404"]
success = 0
fail = 0

for url in url_list:
    print(f"请求URL: {url}")
    try:
        response = requests.get(url,timeout=15)
        print(f"状态码: {response.status_code}")
        if response.status_code == 200:
            print("请求成功")
            success += 1
        else:
            print("请求失败")
            fail += 1
    except requests.exceptions.Timeout:
        print("请求超时，换个网址试试")
        fail += 1
    except requests.exceptions.ConnectionError:
        print("连接失败，检查网络")
        fail += 1
    except requests.exceptions.RequestException as e:
        print(f"其他错误：{e}")
        fail += 1
    print("-" * 30)

print(f"成功: {success}个 失败: {fail}个")