# -*- coding = utf-8 -*-
# @Time : 2023-9-12 20:43
# @Author : Lurume
# @File : newreptile.py
# @Software : PyCharm
import random
import urllib
import requests
from bs4 import BeautifulSoup
import re
import os
import time
import html2text as ht
timu = []
md_maker = ht.HTML2Text()
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.76'
}

#获得网页源代码
def get_html_p(url):
    try:
        r = requests.get(url, timeout=30, headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "error"



# 获取题目
def get_problems(url_p,first):
    htm = get_html_p(url_p)
    soup = BeautifulSoup(htm, "html.parser")
    data_uri = re.findall("decodeURIComponent\(([\s\S]*?)\);window", str(soup))
    data = urllib.parse.unquote(str(data_uri))
    content = bytes(data, 'utf-8').decode('unicode_escape')

    #获取题目
    article = (str(re.findall("h1>([\s\S]*?)</h1", str(soup))))[2:-2]
    timu.append(article)
    elements = soup.find_all('article')
    text = ""
    for element in elements:
        text += str(element)

    #更正部分数学符号转换不正确的问题（实际上还有很多没有转换
    text = re.sub(r'\$(.*?)\$', r'`\1`', text)
    text = re.sub(r'\$(.*?)\$', r'`\1`', text)
    text = re.sub(r'\$(.*?)\$', r'`\1`', text)
    text = re.sub(r'\\lt', r'<', text)
    text = re.sub(r'\\leq', r'<', text)
    text = re.sub(r'\\times', r'×', text)
    text = re.sub(r'\\le', r'≤', text)
    text = re.sub(r'\\longrightarrow', r'⟶', text)
    text = re.sub(r'\\rightarrow', r'⟶', text)
    text = re.sub(r'\\to', r'⟶', text)

    #将html转换为markdown
    text = md_maker.handle(text)

    # 指定文件夹的路径
    folder_path = './data'
    # 要创建的文件夹名称
    new_folder_name = "P" + str(first) + "-" + article
    # 拼接路径
    new_folder_path = os.path.join(folder_path, new_folder_name)
    # 创建文件夹，命名为：题目编号-标题
    if os.path.exists(new_folder_path):
        with open(new_folder_path + "/P" + str(first) + "-" + article + ".md", "w", encoding="utf-8") as f:
            f.write(text)
    else:
        os.mkdir(new_folder_path)
        # 在新建文件夹下新建并写入题目md文件,命名为：题目编号-标题.md
        with open(new_folder_path + "/P" + str(first) + "-" + article + ".md", "w", encoding="utf-8") as f:
            f.write(text)
    time.sleep(random.random())  # 防止被封ip

    return "success"



def main(i=1000):
    url_p = "https://www.luogu.com.cn/problem/P"+str(i)
    get_problems(url_p, i)
    return 'success', timu
