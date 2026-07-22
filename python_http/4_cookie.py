#requests中手动传递cookies和session管理对象cookie的区别

import requests

#手动发送cookies
def manual_cookies():
    url = "http://httpbin.org/get"

    #准备cookies
    my_cookies = {
        "user_id": "10086",
        "login_status": "guest"
    }

    print(f"请求URL: {url}")
    print(f"请求Cookies: {my_cookies}")

    response = requests.get(url, cookies=my_cookies)
    if response.status_code == 200:
        data = response.json()
        received_cookies = data["headers"].get("Cookie")
        print(f"响应Cookies: {received_cookies}")
        print("请求成功")
    else:
        print("请求失败")
        print(response.status_code)

def session_cookies():
    #创建一个session对象
    session = requests.Session()

    #设置cookie
    url_set_cookie = "http://httpbin.org/cookies/set/session_id/998877"
    print(f"设置的Cookie: {url_set_cookie}")
    session.get(url_set_cookie)

    #发起后续请求(Session自动带上之前设置的cookie)
    url_get_info = "http://httpbin.org/get"
    print(f"发起后续请求:{url_get_info}")
    response_1 = session.get(url_get_info)

    if response_1.status_code == 200:
        data = response_1.json()
        received_cookies = data["headers"].get("Cookie")
        print(f"第一次请求收到的Cookies: {received_cookies}")

    #再次发起请求
    response_2 = session.get(url_get_info)
    if response_2.status_code == 200:
        data = response_2.json()
        received_cookies = data["headers"].get("Cookie")
        print(f"第二次请求收到的Cookies: {received_cookies}")

# manual_cookies()
session_cookies()