# -*- codeing = utf-8 -*-
# @File:Bilibili_lucky_Parent_Class.py
# @Software:PyCharm
# @Author:keven
# @Time:2023/5/18 10:22

import sys
sys.path.append('../')  #python文件下有调用当前项目下其他包，避免mac通过终端执行.py时报错找不到文件夹；
# 工作目录不一样：
# 通过pycharm运行，工作目录就是项目位置，pycharm自己封装的一系列操作，拿得到其他包；
# 通过终端执行，工作目录在执行文件位置，系统拿不到同项目下其他包，就会报错
import json
import time
import urllib
from random import randint
import requests
from lxml import etree
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest
import data



class Bilibili_lucky_Parent_Class:


    # 给一个选项类.
    user_option = webdriver.ChromeOptions()

    if sys.platform.startswith('win'):
        print("这是微软系统")
        # 谷歌浏览器个人数据路径
        user_data = r"C:\Users\keven\AppData\Local\Google\Chrome\User Data_bilibili_luck"
        # 添加浏览器用户数据，指定用户数据存储路径
        user_option.add_argument(f"--user-data-dir={user_data}")
        # location放自己chrome.exe的可执行文件地址，指定使用哪个谷歌浏览器
        user_option.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        # 设置浏览器窗口大小
        # user_option.add_argument('window-size=1920,1080')
        # windows系统json文件位置
        # data_local = r"D:\AABCDEFG\PycharmProjects\bilibili_luck\data\luck_url.json"
        # data_local = r"..\data\luck_url.json"

    elif sys.platform.startswith('darwin'):
        print('当前操作系统是Mac OS')
        # 谷歌浏览器个人数据路径
        user_data = r'/Users/bytedance/Documents/config_chrome'
        # 添加浏览器用户数据，指定用户数据存储路径
        user_option.add_argument(f"--user-data-dir={user_data}")
        # location放自己chrome.exe的可执行文件地址，指定使用哪个谷歌浏览器
        user_option.binary_location = r"/Applications/Google_Chrome_bilibili.app/Contents/MacOS/Google Chrome"
        # 设置浏览器窗口大小
        user_option.add_argument('window-size=3840,2160')
        # mac系统json文件位置
        # data_local = r"/Users/bytedance/PycharmProjects/bilibili_luck/data/luck_url.json"
        # data_local = r"../data/luck_url.json"


    # 设置浏览器无界面运行，会加大被防爬发现的概率，不使用
    # user_option.add_argument('headless').
    # 设置窗口启动位置，左上角
    user_option.add_argument('window-position=0,0')
    # 取消浏览器被自动化程序控制的提示
    # user_option.add_argument('disable-infobars')
    user_option.add_experimental_option("excludeSwitches", ['enable-automation'])
    # 设置运行的浏览器使用中文编码
    user_option.add_argument('lang=zh_CN.UTF-8')
    # 谷歌文档提到需要加上这个属性来规避bug，为什么？
    user_option.add_argument('--disable-gpu')
    # 设置加载策略，这是第2种
    # user_option.page_load_strategy = "eager"
    # 实现规避检测，让网站检测不到（可以通过小红书检测）
    user_option.add_argument("--disable-blink-features=AutomationControlled")

    # 实例化谷歌浏览器窗口
    #可能有浏览器驱动报错，重新安装浏览器驱动就可以解决，然后mac系统还需要给信任，设置-隐私与安全-安全性-给信任；
    #注意：检查浏览器驱动的版本和分身浏览器版本是否一致
    web = webdriver.Chrome(options=user_option)
    # web = webdriver.Safari()
    web.maximize_window()

    data_local = "data/luck_url.json"

    # 读取本地json文件，拿到已经跑过的链接
    with open(data_local, "r", encoding="utf-8") as da:
        js = json.load(da)
    # 新建浏览器窗口
    # web.execute_script(f"window.open()")
    # web.switch_to.window(web.window_handles[-1])
    # web.implicitly_wait(3)






