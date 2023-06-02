# -*- codeing = utf-8 -*-
# @File:go_lucky.py
# @Software:PyCharm
# @Author:keven
# @Time:2023/5/18 10:10
import json
import time
import urllib
from random import randint
import requests
from PIL import Image
from lxml import etree
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest


def Go_url(urllist):
    success = 0
    web.get(urllist)
    # web.implicitly_wait(15)
    time.sleep(5)
    # touxiang = ("xpath","//div[@class='bili-dyn-avatar']")
    # WebDriverWait(web,30,1).until(expected_conditions.presence_of_element_located(touxiang))
    action = ActionChains(web)

    # 判断哪种抽奖
    guanfang_lucky = (
    "xpath", "//span[@class='bili-rich-text-module lottery']|//span[@class='opus-text-rich-hl lottery']")
    yuding = ("xpath", "//button[@class='uncheck']")

    try:
        WebDriverWait(web, 2, 1).until(expected_conditions.presence_of_all_elements_located(guanfang_lucky))
        # print("有转发，走官方抽奖\n" + "-"*100)
        # ss = expected_conditions.presence_of_all_elements_located(share)
        # print(WebDriverWait(web,2,1).until(expected_conditions.presence_of_all_elements_located(share)))
        # if len(expected_conditions.presence_of_all_elements_located(share)) > 0:

        # 官方抽奖

        # print(web.current_window_handle)
        # time.sleep(5)
        # driver.find_element("xpath","//div[@class='bili-dyn-avatar']").click()

        # 关注动作：看看有没有关注
        # action.move_to_element(web.find_element("xpath", "//div[@class='reply-box-warp']")).perform()
        # 向下滑动一定距离，让关注按钮出来
        web.execute_script("window.scrollTo(0, 1000)")
        time.sleep(1)

        if len(web.find_elements("xpath",
                                 "//button[@class='bili-follow-button__action bili-button primary bili-button--medium']")) != 0:
            action.click(web.find_element("xpath",
                                          "//button[@class='bili-follow-button__action bili-button primary bili-button--medium']")).perform()
            time.sleep(1)

        # 排除已经删除的抽奖页面
        if len(web.find_elements("xpath", "//a[@class='rollback-btn']")) != 0:
            success = 0
            print("这个抽奖页面已经被删除！")
            return success

        '''action.move_to_element(web.find_element("xpath", "//div[@class='bili-dyn-avatar']")).perform()
        time.sleep(1)

        # 判断是否已经关注，没有的话就关注
        if len(web.find_elements("xpath", "//div[@class='bili-user-profile-view__info__button follow']")) != 0:
            action.click(
                web.find_element("xpath", "//div[@class='bili-user-profile-view__info__button follow']")).perform()
        time.sleep(1)'''

        # 转发动作
        action.move_to_element(web.find_element("xpath", "//div[@class='side-toolbar__action forward']")).perform()
        action.click(web.find_element("xpath", "//div[@class='side-toolbar__action forward']")).perform()
        time.sleep(2)

        action.click(web.find_element("xpath", "//div[@class='bili-dyn-share-publishing__action launcher']")).perform()

        '''action.move_to_element(web.find_element("xpath", "//div[@class='bili-dyn-action forward']")).perform()
        time.sleep(1)

        action.click(web.find_element("xpath", "//div[@class='bili-dyn-action forward']")).perform()
        time.sleep(1)

        action.click(web.find_element("xpath", "//button[@class='bili-dyn-forward-publishing__action__btn']")).perform()
        time.sleep(2)'''
        print("转发成功!\n" + "-" * 100)
        success = 1

        '''time.sleep(2.5)  #切换窗口，没做好
        window_name_list = driver.window_handles
        driver.switch_to.window(window_name_list[-2])'''

        '''#点击关注
        # print(driver.find_element("xpath","//div[@class='h-action']/span[@class='h-f-btn h-follow']"))
        if driver.find_element("xpath","//div[@class='h-action']/span[@class='h-f-btn h-follow']/text()") == "关注" :
            driver.find_element("xpath","//div[@class='h-action']/span[@class='h-f-btn h-follow']").click()'''
    except NoSuchElementException:
        success = 0
        print("这个抽奖页面是转发别人的抽奖！")
        return success
    except TimeoutException:
        try:
            WebDriverWait(web, 2, 1).until(expected_conditions.presence_of_all_elements_located(yuding))

            # 排除已经删除的抽奖页面
            if len(web.find_elements("xpath", "//a[@class='rollback-btn']")) != 0:
                success = 1
                return success

            if len(web.find_elements("xpath", "//button[@class='check']")) != 0:
                print("这里已经预约过，跳过！")
                return 0
            # print("有预约，走官方预约\n" + "-" * 100)
            # elif len(expected_conditions.presence_of_all_elements_located(yuding)) > 0:
            # 预约抽奖
            action.move_to_element(web.find_element("xpath", "//button[@class='uncheck']")).perform()
            action.click(web.find_element("xpath", "//button[@class='uncheck']")).perform()
            print("预约成功!" + "-" * 100)
            success = 1

        except NoSuchElementException:
            success = 0
            print("这个抽奖页面是转发别人的抽奖！")
            return success
        except TimeoutException:
            try:
                # print("没转发，没抽奖，走非官方抽奖\n" + "-" * 100)
                # 关注动作：看看有没有关注
                # action.move_to_element(web.find_element("xpath", "//div[@class='reply-box-warp']")).perform()

                # 排除已经删除的抽奖页面
                if len(web.find_elements("xpath", "//a[@class='rollback-btn']")) != 0:
                    success = 1
                    return success

                web.execute_script("window.scrollTo(0, 1000)")
                time.sleep(1.5)

                if len(web.find_elements("xpath",
                                         "//button[@class='bili-follow-button__action bili-button primary bili-button--medium']")) != 0:
                    action.click(web.find_element("xpath",
                                                  "//button[@class='bili-follow-button__action bili-button primary bili-button--medium']")).perform()
                    time.sleep(1.5)

                '''action.move_to_element(web.find_element("xpath", "//div[@class='bili-dyn-avatar']")).perform()
                time.sleep(1)

                # 判断是否已经关注，没有的话就关注
                if len(web.find_elements("xpath", "//div[@class='bili-user-profile-view__info__button follow']")) != 0:
                    action.click(
                        web.find_element("xpath", "//div[@class='bili-user-profile-view__info__button follow']")).perform()
                time.sleep(1)'''

                # 点击展开评论文本框
                action.move_to_element(web.find_element("xpath", "//textarea[@class='reply-box-textarea']")).perform()
                action.click(web.find_element("xpath", "//textarea[@class='reply-box-textarea']")).perform()
                time.sleep(2)

                # 这里输入文字
                # web.find_element("xpath", "//textarea[@class='reply-box-textarea focus']").clear()
                action.click(web.find_element("xpath", "//textarea[@class='reply-box-textarea focus']")).perform()
                with open("luck_url.json", "r", encoding="utf-8") as da:
                    com = json.load(da)
                web.find_element("xpath", "//textarea[@class='reply-box-textarea focus']").send_keys(com["comment"][randint(0, 10)])
                time.sleep(randint(10, 25))

                action.move_to_element(web.find_element("xpath", "//div[@class='send-text']")).perform()
                action.click(web.find_element("xpath", "//div[@class='send-text']")).perform()
                time.sleep(1.5)

                # 点赞
                action.move_to_element(web.find_element("xpath", "//div[@class='side-toolbar__action like']")).perform()
                action.click(web.find_element("xpath", "//div[@class='side-toolbar__action like']")).perform()
                time.sleep(1.5)

                # 点击转发
                action.move_to_element(
                    web.find_element("xpath", "//div[@class='side-toolbar__action forward']")).perform()
                action.click(web.find_element("xpath", "//div[@class='side-toolbar__action forward']")).perform()
                time.sleep(1.5)

                # 这里输入文字
                web.find_element("xpath", "//div[@class='bili-rich-textarea__inner empty']").clear()

                web.find_element("xpath", "//div[@class='bili-rich-textarea__inner empty']").send_keys("支持~支持~")
                time.sleep(randint(5, 10))
                # 提交转发
                action.click(
                    web.find_element("xpath", "//div[@class='bili-dyn-share-publishing__action launcher']")).perform()
                print("非官方转发成功!" + "-" * 100)
                success = 1
            except NoSuchElementException:
                success = 0
                print("这个抽奖页面是转发别人的抽奖！")
                return success
    time.sleep(2)
    return success