# -*- coding = utf-8 -*-
# @Time : 2023-9-12 10:43
# @Author : Lurume
# @File : reptile_solutions.py
# @Software : PyCharm
import random
import time
import urllib
import requests
from bs4 import BeautifulSoup
import re
import os

url_s = "https://www.luogu.com.cn/problem/solution/P"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.76"
}
re_session = requests.session()

#利用cookie实现自动登录，不知道cookie多久失效，如果失效了就用get_cookie重新获取
def sign_in():
    cookies = [{"domain": "www.luogu.com.cn", "expiry": 1694746192, "httpOnly": False, "name": "C3VK", "path": "/", "sameSite": "Lax", "secure": False, "value": "9915f2"}, {"domain": ".luogu.com.cn", "expiry": 1697337896, "httpOnly": True, "name": "_uid", "path": "/", "sameSite": "None", "secure": True, "value": "790970"}, {"domain": ".luogu.com.cn", "expiry": 1697337870, "httpOnly": True, "name": "__client_id", "path": "/", "sameSite": "None", "secure": True, "value": "5cd170719b47c190fd11d4ddef9bac3e6fa70df7"}]
    for cookie in cookies:
        re_session.cookies.set(cookie['name'], cookie['value'], domain=cookie['domain'], path=cookie['path'],
                               secure=cookie['secure'])
    re_session.headers.update(headers)


def get_html_s(url):
    try:
        r = re_session.get(url)
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "error"

# 获取题解
def get_solutions(first,url_s, timu,index):

    #获取题解
    html = get_html_s(url_s)
    soup = BeautifulSoup(html, "html.parser")
    #获得加密的题解
    data_uri = re.findall("decodeURIComponent\(([\s\S]*?)\);window", str(soup))
    data = urllib.parse.unquote(str(data_uri))
    #解密
    content = bytes(data, 'utf-8').decode('unicode_escape')
    bridge = re.search('content([\s\S]*?)type', content)
    if bridge == None:
        return "error"
    md = bridge.group(1)
    #获得相应的标题
    article = str(timu[index-1])

    # 指定文件夹的路径
    folder_path = './data'
    # 要创建的文件夹名称
    new_folder_name = "P" + str(first) + "-" + article
    # 拼接路径
    new_folder_path = os.path.join(folder_path, new_folder_name)
    with open(new_folder_path + "/P"+str(first)+"-"+article+"-题解.md", "w", encoding="utf-8") as f:
        f.write(md)
    time.sleep(random.random())


    return md


def main(start=1000,end=1050,timu=[]):
    sign_in()
    if end > 1050:
        for i in range(start,end+1):
            mark = get_solutions(i,url_s+str(i),timu,i-start-1)
            while mark == "error":
                print(i,"--error")
            else:
                print(i,"--success")
    return True

# def sign_in(name="18960325385",code="Lurume123"):
#     # 【修改成自己的edgedriver】
#     s = Service(r"./msedgedriver.exe")
#     driver = webdriver.Edge(service=s)
#     driver.get(url_s)
#     driver.refresh()  # 刷新页面
#     driver.maximize_window()  # 浏览器最大化
#     # 对当前页面进行截图
#     driver.save_screenshot('login.png')
#     # 选择验证码图片的元素
#     yzm_btn = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/main/div/div/div/div/div/div/div[3]/div/div[2]/img')
#     # 获取图片元素的位置
#     loc = yzm_btn.location
#     # 获取图片的宽高
#     size = yzm_btn.size
#     # 获取验证码上下左右的位置，电脑的缩放比例125%（100%就不需要乘），需要乘以1.25，否则会出现定位不准确
#     left = loc['x'] * 1.25
#     top = loc['y'] * 1.25
#     right = (loc['x'] + size['width']) * 1.25
#     botom = (loc['y'] + size['height']) * 1.25
#     val = (left, top, right, botom)  # 得到左上右下的值，顺序固定
#     # 打开网页截图
#     login_pic = Image.open('login.png')
#     # 通过左上右下的值，去截取验证码
#     yzm_pic = login_pic.crop(val)
#     # 保存验证码
#     yzm_pic.save('yzm.png')
#     # 识别验证码
#     ocr = ddddocr.DdddOcr(old=True)
#     with open("yzm.png", 'rb') as f:
#         image = f.read()
#     res = ocr.classification(image)
#     print(res)
#     # 填充用户名 密码 验证码 【有id的用id，find_element_by_id替换find_element_by_name】
#
#     driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/main/div/div/div/div/div/div/div[1]/div/input').send_keys(
#         "18960325385")
#     driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/main/div/div/div/div/div/div/div[2]/div/input').send_keys(
#         "Lurume123")
#     driver.find_element(By.XPATH,
#                         '//*[@id="app"]/div[2]/main/div/div/div/div/div/div/div[3]/div/div[1]/input').send_keys(res)
#     # 点击登录
#     driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/main/div/div/div/div/div/div/button').click()
#     time.sleep(1)
#     # 从driver中获取cookie列表(是一个列表，列表的每个元素都是一个字典)
#     # 把cookies设置到session中
#     selenium_user_agent = driver.execute_script("return navigator.userAgent;")
#     print(selenium_user_agent)
#     re_session.headers.update({"user-agent": selenium_user_agent})
#     for cookie in driver.get_cookies():
#         re_session.cookies.set(cookie['name'], cookie['value'])
#     if driver.current_url == "https://www.luogu.com.cn/auth/login":
#         driver.quit()
#         sign_in(name,code)
#     else:
#         return 0
#     # 关闭driver
#     driver.quit()
#     return 1
