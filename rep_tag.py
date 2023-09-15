# -*- coding = utf-8 -*-
# @Time : 2023-9-13 9:51
# @Author : Lurume
# @File : rep_tag.py
# @Software : PyCharm


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
option=webdriver.EdgeOptions()
option.headless=True

url = "https://www.luogu.com.cn/problem/list?page="
pages = 1
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.76"
}
#默认为前五十道题，避免反复爬取
key = {'NOIp 普及组': ['P1002-[NOIP2002 普及组] 过河卒', 'P1008-[NOIP1998 普及组] 三连击', 'P1009-[NOIP1998 普及组] 阶乘之和', 'P1010-[NOIP1998 普及组] 幂次方', 'P1014-[NOIP1999 普及组] Cantor 表', 'P1015-[NOIP1999 普及组] 回文数', 'P1016-[NOIP1999 提高组] 旅行家的预算', 'P1020-[NOIP1999 普及组] 导弹拦截', 'P1022-[NOIP2000 普及组] 计算器的改良', 'P1023-[NOIP2000 普及组] 税收与补贴问题', 'P1028-[NOIP2001 普及组] 数的计算', 'P1029-[NOIP2001 普及组] 最大公约数和最小公倍数问题', 'P1030-[NOIP2001 普及组] 求先序排列', 'P1035-[NOIP2002 普及组] 级数求和', 'P1036-[NOIP2002 普及组] 选数', 'P1037-[NOIP2002 普及组] 产生数', 'P1042-[NOIP2003 普及组] 乒乓球', 'P1043-[NOIP2003 普及组] 数字游戏', 'P1044-[NOIP2003 普及组] 栈', 'P1045-[NOIP2003 普及组] 麦森数', 'P1046-[NOIP2005 普及组] 陶陶摘苹果', 'P1047-[NOIP2005 普及组] 校门外的树', 'P1048-[NOIP2005 普及组] 采药', 'P1049-[NOIP2001 普及组] 装箱问题'], '2002': ['P1002-[NOIP2002 普及组] 过河卒', 'P1031-[NOIP2002 提高组] 均分纸牌', 'P1032-[NOIP2002 提高组] 字串变换', 'P1033-[NOIP2002 提高组] 自由落体', 'P1034-[NOIP2002 提高组] 矩形覆盖', 'P1035-[NOIP2002 普及组] 级数求和', 'P1036-[NOIP2002 普及组] 选数', 'P1037-[NOIP2002 普及组] 产生数'], 'NOIp 提高组': ['P1003-[NOIP2011 提高组] 铺地毯', 'P1004-[NOIP2000 提高组] 方格取数', 'P1005-[NOIP2007 提高组] 矩阵取数游戏', 'P1006-[NOIP2008 提高组] 传纸条', 'P1011-[NOIP1998 提高组] 车站', 'P1012-[NOIP1998 提高组] 拼数', 'P1013-[NOIP1998 提高组] 进制位', 'P1016-[NOIP1999 提高组] 旅行家的预算', 'P1017-[NOIP2000 提高组] 进制转换', 'P1018-[NOIP2000 提高组] 乘积最大', 'P1019-[NOIP2000 提高组] 单词接龙', 'P1021-[NOIP1999 提高组] 邮票面值设计', 'P1024-[NOIP2001 提高组] 一元三次方程求解', 'P1025-[NOIP2001 提高组] 数的划分', 'P1026-[NOIP2001 提高组] 统计单词个数', 'P1027-[NOIP2001 提高组] Car 的旅行路线', 'P1031-[NOIP2002 提高组] 均分纸牌', 'P1032-[NOIP2002 提高组] 字串变换', 'P1033-[NOIP2002 提高组] 自由落体', 'P1034-[NOIP2002 提高组] 矩形覆盖', 'P1038-[NOIP2003 提高组] 神经网络', 'P1039-[NOIP2003 提高组] 侦探推理', 'P1040-[NOIP2003 提高组] 加分二叉树', 'P1041-[NOIP2003 提高组] 传染病控制'], '2011': ['P1003-[NOIP2011 提高组] 铺地毯'], '2000': ['P1004-[NOIP2000 提高组] 方格取数', 'P1017-[NOIP2000 提高组] 进制转换', 'P1018-[NOIP2000 提高组] 乘积最大', 'P1019-[NOIP2000 提高组] 单词接龙', 'P1022-[NOIP2000 普及组] 计算器的改良', 'P1023-[NOIP2000 普及组] 税收与补贴问题'], '2007': ['P1005-[NOIP2007 提高组] 矩阵取数游戏'], '2008': ['P1006-[NOIP2008 提高组] 传纸条'], '1998': ['P1008-[NOIP1998 普及组] 三连击', 'P1009-[NOIP1998 普及组] 阶乘之和', 'P1010-[NOIP1998 普及组] 幂次方', 'P1011-[NOIP1998 提高组] 车站', 'P1012-[NOIP1998 提高组] 拼数', 'P1013-[NOIP1998 提高组] 进制位'], '1999': ['P1014-[NOIP1999 普及组] Cantor 表', 'P1015-[NOIP1999 普及组] 回文数', 'P1016-[NOIP1999 提高组] 旅行家的预算', 'P1020-[NOIP1999 普及组] 导弹拦截', 'P1021-[NOIP1999 提高组] 邮票面值设计'], '2001': ['P1024-[NOIP2001 提高组] 一元三次方程求解', 'P1025-[NOIP2001 提高组] 数的划分', 'P1026-[NOIP2001 提高组] 统计单词个数', 'P1027-[NOIP2001 提高组] Car 的旅行路线', 'P1028-[NOIP2001 普及组] 数的计算', 'P1029-[NOIP2001 普及组] 最大公约数和最小公倍数问题', 'P1030-[NOIP2001 普及组] 求先序排列', 'P1049-[NOIP2001 普及组] 装箱问题'], '2003': ['P1038-[NOIP2003 提高组] 神经网络', 'P1039-[NOIP2003 提高组] 侦探推理', 'P1040-[NOIP2003 提高组] 加分二叉树', 'P1041-[NOIP2003 提高组] 传染病控制', 'P1042-[NOIP2003 普及组] 乒乓球', 'P1043-[NOIP2003 普及组] 数字游戏', 'P1044-[NOIP2003 普及组] 栈', 'P1045-[NOIP2003 普及组] 麦森数'], '2005': ['P1046-[NOIP2005 普及组] 陶陶摘苹果', 'P1047-[NOIP2005 普及组] 校门外的树', 'P1048-[NOIP2005 普及组] 采药'], '字符串': ['P1000-超级玛丽游戏', 'P1012-[NOIP1998 提高组] 拼数', 'P1015-[NOIP1999 普及组] 回文数', 'P1019-[NOIP2000 提高组] 单词接龙', 'P1022-[NOIP2000 普及组] 计算器的改良', 'P1026-[NOIP2001 提高组] 统计单词个数', 'P1030-[NOIP2001 普及组] 求先序排列', 'P1032-[NOIP2002 提高组] 字串变换', 'P1039-[NOIP2003 提高组] 侦探推理', 'P1042-[NOIP2003 普及组] 乒乓球'], '模拟': ['P1001-A+B Problem', 'P1003-[NOIP2011 提高组] 铺地毯', 'P1007-独木桥', 'P1008-[NOIP1998 普及组] 三连击', 'P1014-[NOIP1999 普及组] Cantor 表', 'P1015-[NOIP1999 普及组] 回文数', 'P1022-[NOIP2000 普及组] 计算器的改良', 'P1031-[NOIP2002 提高组] 均分纸牌', 'P1039-[NOIP2003 提高组] 侦探推理', 'P1042-[NOIP2003 普及组] 乒乓球', 'P1046-[NOIP2005 普及组] 陶陶摘苹果', 'P1047-[NOIP2005 普及组] 校门外的树'], '动态规划,dp': ['P1002-[NOIP2002 普及组] 过河卒', 'P1004-[NOIP2000 提高组] 方格取数', 'P1005-[NOIP2007 提高组] 矩阵取数游戏', 'P1006-[NOIP2008 提高组] 传纸条', 'P1018-[NOIP2000 提高组] 乘积最大', 'P1020-[NOIP1999 普及组] 导弹拦截', 'P1026-[NOIP2001 提高组] 统计单词个数', 'P1040-[NOIP2003 提高组] 加分二叉树', 'P1043-[NOIP2003 普及组] 数字游戏', 'P1044-[NOIP2003 普及组] 栈', 'P1048-[NOIP2005 普及组] 采药', 'P1049-[NOIP2001 普及组] 装箱问题'], '枚举': ['P1003-[NOIP2011 提高组] 铺地毯', 'P1008-[NOIP1998 普及组] 三连击', 'P1013-[NOIP1998 提高组] 进制位', 'P1014-[NOIP1999 普及组] Cantor 表', 'P1023-[NOIP2000 普及组] 税收与补贴问题', 'P1024-[NOIP2001 提高组] 一元三次方程求解', 'P1026-[NOIP2001 提高组] 统计单词个数', 'P1029-[NOIP2001 普及组] 最大公约数和最小公倍数问题', 'P1039-[NOIP2003 提高组] 侦探推理', 'P1040-[NOIP2003 提高组] 加分二叉树'], '递归': ['P1004-[NOIP2000 提高组] 方格取数', 'P1016-[NOIP1999 提高组] 旅行家的预算', 'P1028-[NOIP2001 普及组] 数的计算', 'P1030-[NOIP2001 普及组] 求先序排列', 'P1040-[NOIP2003 提高组] 加分二叉树', 'P1049-[NOIP2001 普及组] 装箱问题'], '费用流': ['P1004-[NOIP2000 提高组] 方格取数', 'P1006-[NOIP2008 提高组] 传纸条'], '高精度': ['P1005-[NOIP2007 提高组] 矩阵取数游戏', 'P1009-[NOIP1998 普及组] 阶乘之和', 'P1018-[NOIP2000 提高组] 乘积最大', 'P1037-[NOIP2002 普及组] 产生数', 'P1045-[NOIP2003 普及组] 麦森数'], '进制': ['P1005-[NOIP2007 提高组] 矩阵取数游戏', 'P1013-[NOIP1998 提高组] 进制位', 'P1017-[NOIP2000 提高组] 进制转换'], '贪心': ['P1007-独木桥', 'P1016-[NOIP1999 提高组] 旅行家的预算', 'P1020-[NOIP1999 普及组] 导弹拦截', 'P1031-[NOIP2002 提高组] 均分纸牌'], '数学': ['P1009-[NOIP1998 普及组] 阶乘之和', 'P1010-[NOIP1998 普及组] 幂次方', 'P1011-[NOIP1998 提高组] 车站', 'P1017-[NOIP2000 提高组] 进制转换', 'P1022-[NOIP2000 普及组] 计算器的改良', 'P1023-[NOIP2000 普及组] 税收与补贴问题', 'P1024-[NOIP2001 提高组] 一元三次方程求解', 'P1029-[NOIP2001 普及组] 最大公约数和最小公倍数问题', 'P1033-[NOIP2002 提高组] 自由落体', 'P1035-[NOIP2002 普及组] 级数求和', 'P1044-[NOIP2003 普及组] 栈', 'P1045-[NOIP2003 普及组] 麦森数'], '分治': ['P1010-[NOIP1998 普及组] 幂次方', 'P1024-[NOIP2001 提高组] 一元三次方程求解'], '斐波那契,Fibonacci': ['P1011-[NOIP1998 提高组] 车站'], '排序': ['P1012-[NOIP1998 提高组] 拼数'], '搜索': ['P1013-[NOIP1998 提高组] 进制位', 'P1019-[NOIP2000 提高组] 单词接龙', 'P1021-[NOIP1999 提高组] 邮票面值设计', 'P1025-[NOIP2001 提高组] 数的划分', 'P1032-[NOIP2002 提高组] 字串变换', 'P1034-[NOIP2002 提高组] 矩形覆盖', 'P1036-[NOIP2002 普及组] 选数', 'P1041-[NOIP2003 提高组] 传染病控制', 'P1043-[NOIP2003 普及组] 数字游戏'], '二分': ['P1020-[NOIP1999 普及组] 导弹拦截', 'P1024-[NOIP2001 提高组] 一元三次方程求解', 'P1039-[NOIP2003 提高组] 侦探推理'], '递推': ['P1025-[NOIP2001 提高组] 数的划分', 'P1028-[NOIP2001 普及组] 数的计算', 'P1044-[NOIP2003 普及组] 栈'], '剪枝': ['P1025-[NOIP2001 提高组] 数的划分', 'P1032-[NOIP2002 提高组] 字串变换'], '图论': ['P1027-[NOIP2001 提高组] Car 的旅行路线', 'P1038-[NOIP2003 提高组] 神经网络'], '计算几何': ['P1027-[NOIP2001 提高组] Car 的旅行路线', 'P1034-[NOIP2002 提高组] 矩形覆盖'], '最大公约数,gcd': ['P1029-[NOIP2001 普及组] 最大公约数和最小公倍数问题'], '树形数据结构': ['P1030-[NOIP2001 普及组] 求先序排列'], '深度优先搜索,DFS': ['P1030-[NOIP2001 普及组] 求先序排列', 'P1036-[NOIP2002 普及组] 选数', 'P1037-[NOIP2002 普及组] 产生数'], '广度优先搜索,BFS': ['P1032-[NOIP2002 提高组] 字串变换'], '素数判断,质数,筛法': ['P1036-[NOIP2002 普及组] 选数'], '拓扑排序': ['P1038-[NOIP2003 提高组] 神经网络'], '前缀和': ['P1043-[NOIP2003 普及组] 数字游戏'], '卡特兰数,Catalan': ['P1044-[NOIP2003 普及组] 栈'], '栈': ['P1044-[NOIP2003 普及组] 栈'], '背包': ['P1048-[NOIP2005 普及组] 采药', 'P1049-[NOIP2001 普及组] 装箱问题']}
difficult = {'入门': ['P1000-超级玛丽游戏', 'P1001-A+B Problem', 'P1035-[NOIP2002 普及组] 级数求和', 'P1046-[NOIP2005 普及组] 陶陶摘苹果', 'P1047-[NOIP2005 普及组] 校门外的树'], '普及−': ['P1002-[NOIP2002 普及组] 过河卒', 'P1003-[NOIP2011 提高组] 铺地毯', 'P1008-[NOIP1998 普及组] 三连击', 'P1009-[NOIP1998 普及组] 阶乘之和', 'P1010-[NOIP1998 普及组] 幂次方', 'P1011-[NOIP1998 提高组] 车站', 'P1012-[NOIP1998 提高组] 拼数', 'P1014-[NOIP1999 普及组] Cantor 表', 'P1015-[NOIP1999 普及组] 回文数', 'P1017-[NOIP2000 提高组] 进制转换', 'P1024-[NOIP2001 提高组] 一元三次方程求解', 'P1028-[NOIP2001 普及组] 数的计算', 'P1029-[NOIP2001 普及组] 最大公约数和最小公倍数问题', 'P1030-[NOIP2001 普及组] 求先序排列', 'P1031-[NOIP2002 提高组] 均分纸牌', 'P1036-[NOIP2002 普及组] 选数', 'P1042-[NOIP2003 普及组] 乒乓球', 'P1044-[NOIP2003 普及组] 栈', 'P1048-[NOIP2005 普及组] 采药', 'P1049-[NOIP2001 普及组] 装箱问题'], '普及+/提高': ['P1004-[NOIP2000 提高组] 方格取数', 'P1006-[NOIP2008 提高组] 传纸条', 'P1013-[NOIP1998 提高组] 进制位', 'P1016-[NOIP1999 提高组] 旅行家的预算', 'P1018-[NOIP2000 提高组] 乘积最大', 'P1021-[NOIP1999 提高组] 邮票面值设计', 'P1032-[NOIP2002 提高组] 字串变换', 'P1038-[NOIP2003 提高组] 神经网络', 'P1040-[NOIP2003 提高组] 加分二叉树', 'P1043-[NOIP2003 普及组] 数字游戏'], '提高+/省选−': ['P1005-[NOIP2007 提高组] 矩阵取数游戏', 'P1027-[NOIP2001 提高组] Car 的旅行路线', 'P1034-[NOIP2002 提高组] 矩形覆盖', 'P1039-[NOIP2003 提高组] 侦探推理', 'P1041-[NOIP2003 提高组] 传染病控制'], '普及/提高−': ['P1007-独木桥', 'P1019-[NOIP2000 提高组] 单词接龙', 'P1020-[NOIP1999 普及组] 导弹拦截', 'P1022-[NOIP2000 普及组] 计算器的改良', 'P1023-[NOIP2000 普及组] 税收与补贴问题', 'P1025-[NOIP2001 提高组] 数的划分', 'P1026-[NOIP2001 提高组] 统计单词个数', 'P1033-[NOIP2002 提高组] 自由落体', 'P1037-[NOIP2002 普及组] 产生数', 'P1045-[NOIP2003 普及组] 麦森数']}



def problem_tags(url):
    #启动浏览器，并隐藏窗口
    s = Service(r"./msedgedriver.exe")
    driver = webdriver.Edge(service=s, options=option)
    driver.get(url)
    #获取题目标签
    numbers = driver.find_elements(By.CSS_SELECTOR,"#app > div.main-container > main > div > div > div > div.border.table > div.row-wrap > div > span:nth-child(2)")
    titles = driver.find_elements(By.CSS_SELECTOR,"#app > div.main-container > main > div > div > div > div.border.table > div.row-wrap > div > div.title > a")
    tags = driver.find_elements(By.CLASS_NAME, "tags")
    nandu = driver.find_elements(By.CSS_SELECTOR, "#app > div.main-container > main > div > div > div > div.border.table > div.row-wrap > div > div.difficulty > a > span")
    count = 0
    #遍历标签并把题目分类到字典中
    for tag in tags:
        #关键词分类
        for i in tag.find_elements(By.CLASS_NAME,"lfe-caption"):
            k = i.text.encode('utf-8').decode('unicode_escape')
            T = (numbers[count].text)+"-" + str(titles[count].text).encode('utf-8').decode('unicode_escape')
            if key.get(k) == None:
                key[k]=[T]
            else:
                temp = key[k]
                temp.append(T)
                key[k] = temp
        #难度分类
        if difficult.get(str(nandu[count].text)) == None:
            difficult[str(nandu[count].text)] = [str(numbers[count].text)+"-" + str(titles[count].text)]
        else:
            temp = difficult[str(nandu[count].text)]
            temp.append(str(numbers[count].text)+"-" + str(titles[count].text))
            difficult[str(nandu[count].text)] = temp
        count = count + 1
    #点击显示算法按钮切换标签
    driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/main/div/div/div/div[1]/div[1]/div/div[4]/span/a').click()
    tags = driver.find_elements(By.CLASS_NAME, "tags")
    count = 0
    #重复爬取
    for tag in tags:
        for i in tag.find_elements(By.CLASS_NAME, "lfe-caption"):
            k = i.text.encode('utf-8').decode('unicode_escape')
            T = (numbers[count].text) + "-" + str(titles[count].text).encode('utf-8').decode('unicode_escape')
            if key.get(k) == None:
                key[k] = [T]
            else:
                temp = key[k]
                temp.append(T)
                key[k] = temp
        count = count + 1


def main(start=1000,end=1049):
    global key, difficult, pages
    #根据输入的题目范围计算所在目录页数
    if start >= 1000 and end <= 1049:
       return difficult, key
    else:
        for i in range(int((start-950)/50), int((end-950)/50)+1):
            url = "https://www.luogu.com.cn/problem/list?page=" + str(i)
            problem_tags(url)
        return difficult, key