# -*- codeing = utf-8 -*-
# @File:test_Go_url.py
# @Software:PyCharm
# @Author:keven
# @Time:2023/5/30 15:34
import json
import time
from random import randint
import pytest
from selenium.webdriver import ActionChains
from method.Bilibili_lucky_Parent_Class import Bilibili_lucky_Parent_Class as tbl


class Test_Go_url(tbl):
    action = ActionChains(tbl.web)

    def test_go_url_GF(self):
        print("这是官方抽奖页面，run......")

        # 排除已经删除的抽奖页面
        if len(tbl.web.find_elements("css selector", "a[class='rollback-btn']")) != 0:
            print("这个抽奖页面已经被删除！")
            return 0

        # 向下滑动一定距离，让关注按钮出来
        tbl.web.execute_script("window.scrollTo(0, 1000)")
        time.sleep(1)

        # 判断是否已经关注
        if len(tbl.web.find_elements("css selector",
                                     "button[class='bili-follow-button__action bili-button primary bili-button--medium']")) != 0:
            Test_Go_url.action.click(tbl.web.find_element("css selector",
                                                     "button[class='bili-follow-button__action bili-button primary bili-button--medium']")).perform()
            time.sleep(1)

        # 转发动作
        Test_Go_url.action.move_to_element(
            tbl.web.find_element("css selector", "div[class='side-toolbar__action forward']")).perform()
        Test_Go_url.action.click(tbl.web.find_element("css selector", "div[class='side-toolbar__action forward']")).perform()
        time.sleep(2)

        Test_Go_url.action.click(
            tbl.web.find_element("css selector", "div[class='bili-dyn-share-publishing__action launcher']")).perform()
        time.sleep(1.5)

        # 有出现这个消息提示
        # bili-dyn-share-succ-tip__tips
        # tbl.web.find_element("xpath","//div[@class='bili-dyn-share-succ-tip']")
        assert len(tbl.web.find_elements("xpath","//div[@class='bili-dyn-share-succ-tip']")) > 0,f"官方抽奖页面转发后没有出现成功的提示！！！"
        # pytest.main(["-v","-s"])
        print("转发成功!\n" + "-" * 100)

        return 1

    def test_go_url_YY(self):
        print("这是预约抽奖页面，run......")

        if len(tbl.web.find_elements("css selector", "button[class='uncheck']")) > 0:
            # 排除已经删除的抽奖页面
            if len(tbl.web.find_elements("css selector", "a[class='rollback-btn']")) != 0:
                return 0
            #     排除撤销预约的页面
            elif len(tbl.web.find_elements("css selector", "button[class='check disabled']")) != 0:
                return 0

            if len(tbl.web.find_elements("css selector", "button[class='check']")) != 0:
                print("这里已经预约过，跳过！")
                return 0

            # 预约抽奖
            Test_Go_url.action.move_to_element(tbl.web.find_element("css selector", "button[class='uncheck']")).perform()
            Test_Go_url.action.click(tbl.web.find_element("css selector", "button[class='uncheck']")).perform()
            time.sleep(1.5)
            # 有出现这个消息提示
            # tbl.web.find_element("xpath","//div[@class='bili-message__content']")
            assert len(tbl.web.find_elements("xpath","//div[@class='bili-message__content']")) > 0,f"预约后没有出现预约成功提示！！！"
            print("预约成功!" + "-" * 100)

            return 1
        else:
            print("预约过，可能是因为某种原因暂停，还没有写入json")

            return 0


    def test_go_url_FGF_new(self):
        print("这是非官方抽奖新页面，run......")

        # 排除已经删除的抽奖页面
        if len(tbl.web.find_elements("css selector", "a[class='rollback-btn']")) != 0:
            return 0
        #     排除撤销预约的页面
        elif len(tbl.web.find_elements("css selector", "button[class='check disabled']")) != 0:
            return 0

        # 先获得有没有话题,滑动到下面后不好获取
        huati = tbl.web.find_elements("xpath",
                                      "//a[@class='opus-text-rich-hl topic']")
        pinglun = ""
        neiron = tbl.web.find_element("xpath",
                                      "//div[@class='opus-module-content']").get_attribute("innerText")  # 获取div标签的文本

        # 向下滑动，展示关注按钮
        tbl.web.execute_script("window.scrollTo(0, 1000)")
        time.sleep(1.5)

        # 判断是否关注
        if len(tbl.web.find_elements("css selector",
                                     "button[class='bili-follow-button__action bili-button primary bili-button--medium']")) != 0:
            Test_Go_url.action.click(tbl.web.find_element("css selector",
                                                     "button[class='bili-follow-button__action bili-button primary bili-button--medium']")).perform()
            time.sleep(1.5)

        # 向下滑动一定距离，加载评论区
        tbl.web.execute_script("window.scrollTo(0, 1000)")
        time.sleep(1)

        # 先定位到评论区，不然拿不到评论元素
        Test_Go_url.action.click(tbl.web.find_element("css selector", "div[class='side-toolbar__action comment']")).perform()

        # 点击展开评论文本框
        Test_Go_url.action.move_to_element(
            tbl.web.find_element("css selector", "textarea[class='reply-box-textarea']")).perform()
        Test_Go_url.action.click(tbl.web.find_element("css selector", "textarea[class='reply-box-textarea']")).perform()
        time.sleep(2)

        Test_Go_url.action.click(
            tbl.web.find_element("css selector", "textarea[class='reply-box-textarea focus']")).perform()
        with open(tbl.data_local, "r", encoding="utf-8") as da:
            com = json.load(da)

        # 判断是否需要带话题评论，输入评论
        if "带话题" in neiron or "带" in neiron:
            for i, ii in enumerate(huati):
                pinglun = pinglun + huati[i].get_attribute("textContent")  # 获取a标签的文本，但这里是span标签
            tbl.web.find_element("css selector", "textarea[class='reply-box-textarea focus']").send_keys(
                com["bilibili_comment"][randint(0, 17)] + pinglun)
        else:
            tbl.web.find_element("css selector", "textarea[class='reply-box-textarea focus']").send_keys(
                com["bilibili_comment"][randint(0, 17)])
        time.sleep(randint(2, 10))

        # 点击发送
        Test_Go_url.action.move_to_element(tbl.web.find_element("css selector", "div[class='send-text']")).perform()
        Test_Go_url.action.click(tbl.web.find_element("css selector", "div[class='send-text']")).perform()
        time.sleep(1.5)

        # 点赞
        if len(tbl.web.find_elements("css selector", "div[class='side-toolbar__action like']")) > 0:
            Test_Go_url.action.move_to_element(
                tbl.web.find_element("css selector", "div[class='side-toolbar__action like']")).perform()
            Test_Go_url.action.click(
                tbl.web.find_element("css selector", "div[class='side-toolbar__action like']")).perform()
            time.sleep(1.5)

        # 点击转发
        Test_Go_url.action.move_to_element(
            tbl.web.find_element("css selector", "div[class='side-toolbar__action forward']")).perform()
        Test_Go_url.action.click(tbl.web.find_element("css selector", "div[class='side-toolbar__action forward']")).perform()
        time.sleep(1.5)

        # 这里输入文字
        tbl.web.find_element("css selector", "div[class='bili-rich-textarea__inner empty']").clear()
        if "带话题" in neiron or "带" in neiron:
            tbl.web.find_element("css selector", "div[class='bili-rich-textarea__inner empty']").send_keys(
                "支持~支持~" + pinglun)
        else:
            tbl.web.find_element("css selector", "div[class='bili-rich-textarea__inner empty']").send_keys("支持~支持~")

        # tbl.web.find_element("css selector", "div[class='bili-rich-textarea__inner empty']").send_keys("支持~支持~")
        time.sleep(randint(1, 3))

        # 提交转发
        Test_Go_url.action.click(
            tbl.web.find_element("css selector", "div[class='bili-dyn-share-publishing__action launcher']")).perform()
        time.sleep(1.5)
        # 有出现这个消息提示
        # tbl.web.find_element("xpath","//div[@class='bili-message__content']")
        assert len(tbl.web.find_elements("xpath","//div[@class='bili-dyn-share-succ-tip']")) > 0 ,f"非官方新页面转发后没有出现成功提示！！！"
        print("非官方新页面转发成功!\n" + "-" * 100)

        return 1

    def test_go_url_FGF_old(self):
        print("这是非官方旧抽奖页面，run......")

        # 排除已经删除的抽奖页面
        if len(tbl.web.find_elements("css selector", "a[class='rollback-btn']")) != 0:
            return 0

        # 非官方，旧页面关注动作
        forw1 = tbl.web.find_elements("css selector",
                                      "div[class='bili-dyn-content__forw__desc'] span[class='bili-rich-text-module at']")
        forw2 = tbl.web.find_elements("css selector",
                                      "div[class='bili-dyn-content__orig__desc'] span[class='bili-rich-text-module at']")

        for i, f1 in enumerate(forw1):
            Test_Go_url.action.move_to_element(forw1[i]).perform()
            time.sleep(1)
            if len(tbl.web.find_elements("css selector",
                                         "div[class='bili-user-profile-view__info__button follow']")) > 0:
                Test_Go_url.action.click(tbl.web.find_element("css selector",
                                                         "div[class='bili-user-profile-view__info__button follow']")).perform()

        for i, f1 in enumerate(forw2):
            Test_Go_url.action.move_to_element(forw2[i]).perform()
            time.sleep(1)
            if len(tbl.web.find_elements("css selector",
                                         "div[class='bili-user-profile-view__info__button follow']")) > 0:
                Test_Go_url.action.click(tbl.web.find_element("css selector",
                                                         "div[class='bili-user-profile-view__info__button follow']")).perform()

        # 先获得有没有话题,滑动到下面后不好获取
        huati = tbl.web.find_elements("xpath",
                                      "//div[@class='bili-dyn-content__forw__desc']//span[@class='bili-rich-text-topic']")
        pinglun = ""
        neiron = ""
        if len(tbl.web.find_elements("xpath", "//div[@class='bili-dyn-content__forw__desc']")) > 0:
            neiron = tbl.web.find_element("xpath", "//div[@class='bili-dyn-content__forw__desc']").get_attribute(
                "innerText")  # 获取div标签的文本
        else:
            neiron = tbl.web.find_element("xpath", "//div[@class='bili-dyn-content__orig']").get_attribute(
                "innerText")  # 获取div标签的文本

        # 向下滑动一定距离，加载评论区
        tbl.web.execute_script("window.scrollTo(0, 1000)")
        time.sleep(2)

        # 点赞
        if len(tbl.web.find_elements("css selector", "div[class='bili-dyn-action like']")) > 0:
            Test_Go_url.action.move_to_element(
                tbl.web.find_element("css selector", "div[class='bili-dyn-action like']")).perform()
            Test_Go_url.action.click(tbl.web.find_element("css selector", "div[class='bili-dyn-action like']")).perform()
            time.sleep(1.5)

        # 点击展开评论文本框
        Test_Go_url.action.move_to_element(
            tbl.web.find_element("css selector", "textarea[class='ipt-txt']:nth-child(2)")).perform()
        Test_Go_url.action.click(tbl.web.find_element("css selector", "textarea[class='ipt-txt']:nth-child(2)")).perform()
        time.sleep(1)

        # 这里输入文字
        # Go_url.action.click(tbl.web.find_element("css selector", "textarea[class='ipt-txt']")).perform()
        with open(tbl.data_local, "r", encoding="utf-8") as da:
            com = json.load(da)

        # 判断是否需要带话题评论
        if "带话题" in neiron or "带" in neiron:
            for i, ii in enumerate(huati):
                pinglun = pinglun + huati[i].get_attribute("textContent")  # 获取a标签的文本，但这里是span标签
            tbl.web.find_element("css selector", "textarea[class='ipt-txt']:nth-child(2)").send_keys(
                com["bilibili_comment"][randint(0, 17)] + pinglun)
        else:
            tbl.web.find_element("css selector", "textarea[class='ipt-txt']:nth-child(2)").send_keys(
                com["bilibili_comment"][randint(0, 17)])
        time.sleep(randint(2, 10))

        # 勾选同时转发
        Test_Go_url.action.click(tbl.web.find_element("css selector", "div[class='dynamic-repost']")).perform()
        time.sleep(0.5)

        # 发送
        Test_Go_url.action.click(tbl.web.find_element("css selector", "button[class='comment-submit']")).perform()
        time.sleep(0.5)

        # 有出现这个消息提示
        # tbl.web.find_element("xpath","//div[@class='bili-message__content']")
        assert len(tbl.web.find_elements("xpath","//div[@class='mini']")) > 0 ,f"非官方旧页面转发成功后没有出现成功提示！！！"
        print("非官方旧页面转发成功!\n" + "-" * 100)

        return 1


    def test_go_url_WB(self):
        print("这是微博抽奖链接，run......")
        time.sleep(1)

        # 判断是否关注
        if len(tbl.web.find_elements("xpath",
                                     "//button[@class='woo-button-main woo-button-line woo-button-primary woo-button-s woo-button-round follow-btn_followbtn_FNC50']")) > 0:
            Test_Go_url.action.click(tbl.web.find_element("xpath",
                                                     "//button[@class='woo-button-main woo-button-line woo-button-primary woo-button-s woo-button-round follow-btn_followbtn_FNC50']")).perform()
            time.sleep(2)

        # 先获取页面中出现的微博号，一个一个关注
        guanzhu2 = tbl.web.find_elements("xpath", "//div[@class='wbpro-feed-content']//a[contains(@href,'/n/')]")
        gzhu_url = []
        # 获取当前博主的微博名字，关注的时候去重
        weibo_zhu = tbl.web.find_element("xpath",
                                         "//a[@class='ALink_default_2ibt1 head_cut_2Zcft head_name_24eEB']/span").get_attribute(
            "innerText")
        weibo_gf = "@微博抽奖平台"

        if len(guanzhu2) > 0:
            for i, qq in enumerate(guanzhu2):
                gzhu_url.append(guanzhu2[i].get_attribute("href"))

            for i, qi in enumerate(guanzhu2):
                # 判断去重，当前博主和微博抽奖平台不操作关注
                if weibo_zhu in guanzhu2[i].get_attribute("innerText") or weibo_gf in guanzhu2[i].get_attribute(
                        "innerText"):
                    continue
                tbl.web.get(gzhu_url[i])
                time.sleep(2)

                if len(tbl.web.find_elements("xpath",
                                             "//button[@class='woo-button-main woo-button-flat woo-button-primary woo-button-m woo-button-round FollowBtn_m_1UJhp ProfileHeader_btn3_2VD_Y']")) > 0:
                    Test_Go_url.action.click(tbl.web.find_element("xpath",
                                                             "//button[@class='woo-button-main woo-button-flat woo-button-primary woo-button-m woo-button-round FollowBtn_m_1UJhp ProfileHeader_btn3_2VD_Y']")).perform()
                time.sleep(1)
                # 关注完成，回到原微博
                tbl.web.back()

        # 判断是否点赞
        Test_Go_url.action.move_to_element(tbl.web.find_element("css selector",
                                                           "div[class='woo-box-item-flex toolbar_item_1ky_D toolbar_cursor_34j5V']")).perform()
        if len(tbl.web.find_elements("css selector", "span[class='woo-like-iconWrap']")) > 0:
            Test_Go_url.action.click(tbl.web.find_element("css selector", "span[class='woo-like-iconWrap']")).perform()
            time.sleep(2)

        # 转发
        Test_Go_url.action.move_to_element(tbl.web.find_element("css selector",
                                                           "div[class='woo-box-flex woo-box-alignCenter woo-box-justifyCenter toolbar_wrap_np6Ug']")).perform()
        Test_Go_url.action.click(
            tbl.web.find_element("css selector",
                                 "div[class='woo-box-flex woo-box-alignCenter woo-box-justifyCenter toolbar_wrap_np6Ug']")).perform()
        time.sleep(1)
        Test_Go_url.action.move_to_element(
            tbl.web.find_element("css selector", "textarea[class='Form_input_3JT2Q']")).perform()
        with open(tbl.data_local, "r", encoding="utf-8") as da:
            com = json.load(da)

        # 判断是否需要带话题评论
        huati = tbl.web.find_elements("xpath", "//div[@class='detail_wbtext_4CRf9']/a[contains(@href,'s.weibo')]")
        pinglun = ""
        neiron = tbl.web.find_element("xpath", "//div[@class='wbpro-feed-content']").get_attribute(
            "innerText")  # 获取div标签的文本
        if "带话题" in neiron or "带" in neiron:
            for i, ii in enumerate(huati):
                pinglun = pinglun + huati[i].get_attribute("textContent")  # 获取a标签的文本
            tbl.web.find_element("css selector", "textarea[class='Form_input_3JT2Q']").send_keys(
                com["weibo_comment"][randint(0, 17)] + pinglun)
        else:
            tbl.web.find_element("css selector", "textarea[class='Form_input_3JT2Q']").send_keys(
                com["weibo_comment"][randint(0, 17)])
        time.sleep(randint(2, 10))

        # 同时勾选评论
        Test_Go_url.action.click(
            tbl.web.find_element("css selector", "span[class='woo-checkbox-shadow']")).perform()
        time.sleep(1)

        # 点击发送评论和转发
        Test_Go_url.action.click(
            tbl.web.find_element("css selector",
                                 "button[class='disabled woo-button-main woo-button-flat woo-button-primary woo-button-m woo-button-round Composer_btn_2XFOD']")).perform()
        print("微博抽奖转发成功!" + "-" * 100)

        return 1