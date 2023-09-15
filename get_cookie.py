from selenium import webdriver
import os
import time
import json
import re
from PIL import Image
import ddddocr
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
########步骤一##########
def get_cookies():
    """
    获取cookies保存至本地
    """
    log_url = 'https://www.luogu.com.cn/auth/login'
    os.chdir(r'D:\Desktop\all')
    #【修改成自己的edgedriver】
    s = Service(r"./msedgedriver.exe")
    driver = webdriver.Edge(service=s)
    driver.get(log_url)
    driver.refresh()  # 刷新页面
    driver.maximize_window()  # 浏览器最大化
    # 对当前页面进行截图
    driver.save_screenshot('login.png')
    # 选择验证码图片的元素
    yzm_btn = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/main/div/div/div/div/div/div/div[3]/div/div[2]/img')
    # 获取图片元素的位置
    loc = yzm_btn.location
    # 获取图片的宽高
    size = yzm_btn.size
    # 获取验证码上下左右的位置，电脑的缩放比例125%（100%就不需要乘），需要乘以1.25，否则会出现定位不准确
    left = loc['x'] * 1.25
    top = loc['y'] * 1.25
    right = (loc['x'] + size['width']) * 1.25
    botom = (loc['y'] + size['height']) * 1.25
    val = (left, top, right, botom)  # 得到左上右下的值，顺序固定
    # 打开网页截图
    login_pic = Image.open('login.png')
    # 通过左上右下的值，去截取验证码
    yzm_pic = login_pic.crop(val)
    # 保存验证码
    yzm_pic.save('yzm.png')
    # 识别验证码
    ocr = ddddocr.DdddOcr(old=True)
    with open("yzm.png", 'rb') as f:
        image = f.read()
    res = ocr.classification(image)
    print(res)
    # 填充用户名 密码 验证码 【有id的用id，find_element_by_id替换find_element_by_name】

    driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/main/div/div/div/div/div/div/div[1]/div/input').send_keys(
        "18960325385")
    driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/main/div/div/div/div/div/div/div[2]/div/input').send_keys(
        "Lurume123")
    driver.find_element(By.XPATH,
                        '//*[@id="app"]/div[2]/main/div/div/div/div/div/div/div[3]/div/div[1]/input').send_keys(res)
    # 点击登录
    driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/main/div/div/div/div/div/div/button').click()
    time.sleep(5)
    if driver.current_url == "https://www.luogu.com.cn/auth/login":
        driver.quit()
        get_cookies()
    dictCookies = driver.get_cookies()  # 获取list的cookies
    jsonCookies = json.dumps(dictCookies)  # 转换成字符串保存
    re.sub('true', 'True', jsonCookies)
    re.sub('false', 'False', jsonCookies)

    with open('damai_cookies.txt', 'w') as f:
        f.write(jsonCookies)
    print('cookies保存成功！')


if __name__ == "__main__":
    get_cookies()