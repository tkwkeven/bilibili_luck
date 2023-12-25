# -*- codeing = utf-8 -*-
# @File:Get_lucky_list.py
# @Software:PyCharm
# @Author:keven
# @Time:2023/5/18 10:38
import time
from selenium.webdriver import ActionChains
from method.Bilibili_lucky_Parent_Class import Bilibili_lucky_Parent_Class as tbl


class Get_luck_list(tbl):
    action = ActionChains(tbl.web)
    def get_luck_list(self,luck_meesage,type):
        tbl.web.get(luck_meesage)
        res = []
        action = ActionChains(tbl.web)
        # tbl.web.switch_to.window(tbl.web.window_handles[-1])

        # 第一种页面获取抽奖链接--------------哔哩哔哩
        if type == 1 :
            # 截图
            # web.get_screenshot_as_file("jietu.png")
            time.sleep(3)
            dianji_url = tbl.web.find_element("css selector", "div[class='msg-push-new']:last-child a").get_attribute("href")
            tbl.web.get(dianji_url)
            url_list_sele = tbl.web.find_elements("css selector","div[class='article-content'] a[href*='t.bilibili'],div[class='article-content'] a[href*='www.bilibili']")
            for i,ur in enumerate(url_list_sele):
                res.append(url_list_sele[i].get_attribute("href"))


        # 第二种页面获取抽奖链接--------------哔哩哔哩
        elif type == 2 :
            time.sleep(3)
            # 向上滑动2次，拿到两次加载后的链接；getElementsByClassName返回的是一个列表，所以要用[0]下标
            tbl.web.execute_script("var q=document.getElementsByClassName('message-list')[0].scrollTop=0")
            time.sleep(1)
            tbl.web.execute_script("var q=document.getElementsByClassName('message-list')[0].scrollTop=0")
            time.sleep(1)
            tbl.web.execute_script("var q=document.getElementsByClassName('message-list')[0].scrollTop=0")
            time.sleep(1)

            links = tbl.web.find_elements("css selector","a[class='dynamic-link']")
            for i,url in enumerate(links):
                res.append(links[i].get_attribute("href"))

        # 第三种页面获取抽奖链接：专栏页面--------------哔哩哔哩
        elif type == 3:
            time.sleep(2)
            # 拿到专栏中前两个动态
            # dianji_urls = tbl.web.find_elements("css selector", "div[class='main-content'] div:nth-child(-n+2) div[class='content'] li:nth-child(-n+2) h2 a")
            # print(dianji_urls[1].get_attribute("href"), "\n")  //循环开始前，专栏前两个动态链接获取正常

            # 原方法2023年11月01号左右失效，报错元素已经过时，循环第2次时无法正常获取专栏中第2个动态链接
            # for i,uo in enumerate(dianji_urls):
            #     time.sleep(1)
            #     url = dianji_urls[i].get_attribute("href")
            #     # Get_luck_list.action.click(dianji_urls[i]).perform()
            #     tbl.web.get(url)
            #     time.sleep(1)
            #     url_list_sele = tbl.web.find_elements("css selector",
            #                                           "div[class='article-content'] a[href*='t.bilibili'],div[class='article-content'] a[href*='www.bilibili'],div[class='article-content'] a[href*='b23']")
            #     for i, ur in enumerate(url_list_sele):
            #         res.append(url_list_sele[i].get_attribute("href"))
            #
            #     # 返回上一页，不然获取不到专栏中第二个动态
            #     tbl.web.back()

            # 新方法，变更点1：每次循环重新获取对应的元素；变更点2：强制返回2次（解决某个专栏中动态页面地址多跳转1次的问题）-》https://space.bilibili.com/3493086911007529/article
            i = 0
            while i < 2:
                time.sleep(1)
                # dianji_urls = tbl.web.find_elements("css selector",
                # 旧浏览器版本样式布局，下方为新版本浏览器样式                                    "div[class='main-content'] div:nth-child(-n+2) div[class='content'] li:nth-child(-n+2) h2 a")
                dianji_urls = tbl.web.find_elements("css selector",
                                                    "div[class='container'] div[class='item'] div[class='article-card'] a,div[class='container'] div[class='item'] div[class='article-card article-card__no-img'] a")

                url = dianji_urls[i].get_attribute("href")
                tbl.web.get(url)
                time.sleep(1)
                url_list_sele = tbl.web.find_elements("css selector",
                                                      "div[class='article-content'] a[href*='t.bilibili'],div[class='article-content'] a[href*='www.bilibili'],div[class='article-content'] a[href*='b23']")
                for i, ur in enumerate(url_list_sele):
                    res.append(url_list_sele[i].get_attribute("href"))

                # 返回上一页，不然获取不到专栏中第二个动态
                tbl.web.back()
                # tbl.web.back()
                i += 1


        # 微博抽奖页面：集合微博----------------微博
        elif type == 4:
            time.sleep(3)
            # 点击展开，才能获取微博全部的链接
            zhankai = tbl.web.find_elements("xpath","//div[@class='vue-recycle-scroller__item-wrapper']/div[position()<4]//span[@class='expand']")
            if len(zhankai) >0 :
                # for i, uu in enumerate(zhankai):
                action.move_to_element(zhankai[0]).perform()
                action.click(zhankai[0]).perform()
                # 展开后定位不到下个元素，往下滑一下
                # tbl.web.execute_script("window.scrollTo(0, 2500)")
                time.sleep(1)
            # 获取微博中的抽奖链接，只取有抽奖链接的微博，筛选一下
            shaixuan = tbl.web.find_elements("xpath","//div[@class='vue-recycle-scroller__item-view']//div[contains(text(),'抽奖合集')]|//div[@class='vue-recycle-scroller__item-view']//div[contains(text(),'抽奖集合')]")
            # heji = shaixuan[0].find_elements("xpath","//a[contains(@href,'weibo')][not(@title)][contains(text(),'微博正文')]|//a[contains(@href,'detail')]")
            heji = shaixuan[0].find_elements("css selector","a[href*='weibo']:not([title]),a[href*='detail']")
            for i,uq in enumerate(heji):
                res.append(heji[i].get_attribute("href"))


        # 小红书抽奖页面：小红书集合---------------------小红书
        elif type == 5:
            time.sleep(2)
            dianji_url = tbl.web.find_element("xpath",
                                               "//section[position()<4]//a[@class='cover ld']").get_attribute("href")
            print(dianji_url)
            # for i, ur in enumerate(dianji_url):
            #     res.append(dianji_url[i].get_attribute("href"))





        return res
