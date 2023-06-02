# -*- codeing = utf-8 -*-
# @File:oooo.py
# @Software:PyCharm
# @Author:keven
# @Time:2023/5/4 15:52


import time
from shibie import base64_api
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from PIL import Image

tart = time.time()
s = Service('chromedriver.exe')

bro = webdriver.Chrome(service=s)
bro.maximize_window()
bro.get('https://passport.bilibili.com/login')
u = bro.find_element(By.ID, 'login-username')
p = bro.find_element(By.ID, 'login-passwd')
btn = bro.find_element(By.CSS_SELECTOR, '.btn-login')
time.sleep(1)
u.send_keys('你的B站账号')
time.sleep(1)
p.send_keys('你的B站密码')
btn.click()
time.sleep(2)
# 截屏
bro.save_screenshot('aa.png')
code_img_ele = bro.find_element(By.CSS_SELECTOR, '.geetest_panel_next')
# 验证码图片左上角的坐标 x,y
location = code_img_ele.location
print('location', location)
# 验证码标签对应的长和宽
size = code_img_ele.size
print('size:', size)
# 左上角和右下角坐标
rangle = (
    int(location['x']), int(location['y']), int(location['x'] + size['width']), int(location['y'] + size['height']))
# 至此验证码图片区域就确定下来了

# 裁剪图片
i = Image.open('../../method/aa.png')
code_img_name = 'code.png'
# crop根据指定区域进行图片裁剪
frame = i.crop(rangle)
frame.save(code_img_name)

result = base64_api('你的账号', '你的密码', code_img_name, 27)
print(result)
# time.sleep(2)
pos_lst = [k.split(',') for k in result.split('|')]

# 设置动作链
action = ActionChains(bro)
for x, y in pos_lst:
    action.move_to_element_with_offset(code_img_ele, x, y).click().perform()
action.release()
# time.sleep(2)
btn2 = bro.find_element(By.CSS_SELECTOR, '.geetest_commit_tip')
btn2.click()
time.sleep(3)
print(time.time() - tart)