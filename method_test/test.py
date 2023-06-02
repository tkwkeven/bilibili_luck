import sys

sys.path.append('../')  #python文件下有调用当前项目下其他包，避免mac通过终端执行.py时报错找不到文件夹；工作目录不一样：通过pycharm运行，工作目录就是项目位置，pycharm自己封装的一系列操作，拿得到其他包；通过终端执行，工作目录在执行文件位置，系统拿不到同项目下其他包，就会报错
# -*- codeing = utf-8 -*-
# @File:test.py
# @Software:PyCharm
# @Author:keven
# @Time:2023/4/28 16:41
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

Url = "https://www.bilibili.com/read/cv23351892"
# 谷歌浏览器个人数据路径
user_data = r'/Users/bytedance/Documents/config_chrome'
# 给一个选项类
user_option = webdriver.ChromeOptions()
# 添加浏览器用户数据
user_option.add_argument(f"--user-data-dir={user_data}")

#location放自己chrome.exe的可执行文件地址
user_option.binary_location = r"/Applications/Google_Chrome_bilibili.app/Contents/MacOS/Google Chrome"
# 设置浏览器无界面运行
# user_option.add_argument('headless')
user_option.add_argument('window-size=3840,2160')
# 设置窗口启动位置，左上角
user_option.add_argument('window-position=0,0')
# 取消浏览器被自动化程序控制的提示
# user_option.add_argument('disable-infobars')
user_option.add_experimental_option("excludeSwitches", ['enable-automation'])
# 使用中文编码
user_option.add_argument('lang=zh_CN.UTF-8')
# 谷歌文档提到需要加上这个属性来规避bug
user_option.add_argument('--disable-gpu')

# 实例化谷歌浏览器窗口,指定使用的浏览器
web = webdriver.Chrome(options=user_option)
# web = webdriver.Safari()
# web.maximize_window()


def Get_luck_list(luck_meesage,type):
    web.get(luck_meesage)
    res = []
    if type == 1 :
        # time.sleep(3)
        web.implicitly_wait(10)
        action = ActionChains(web)
        # web.get_screenshot_as_file("jietu.png")
        action.click(web.find_element("xpath", "//div[@class='msg-push-new'][last()]/a")).perform()
        # time.sleep(3)
        # res = web.find_element("xpath", "//div[@class='msg-push-new'][last()]/a").get_attribute("href")
        web.switch_to.window(web.window_handles[-1])
        # time.sleep(3)
        url_list_sele = web.find_elements("xpath","//div[@class='article-content']//a[contains(@href,'t.bilibili')]|//div[@class='article-content']//a[contains(@href,'www.bilibili')]")
        for i,ur in enumerate(url_list_sele):
            res.append(url_list_sele[i].get_attribute("href"))
    elif type == 2 :
        web.implicitly_wait(10)
        links = web.find_elements("xpath","//a[@class='dynamic-link']")
        for i,url in enumerate(links):
            res.append(links[i].get_attribute("href"))
    return res


# 获得所有抽奖的url
def Get_Luck_Url_html(Url,type):
    # 模拟头部信息
    head = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
    }

    if type == 1:
        Request = urllib.request.Request(Url, headers=head)
        html = ""
        try:
            Response = urllib.request.urlopen(Request)
            html = Response.read().decode("utf-8")

            result = etree.HTML(html).xpath(
                "//div[@class='article-content']//a[contains(@href,'t.bilibili')]/@href|//div[@class='article-content']//a[contains(@href,'www.bilibili')]/@href")
        except urllib.error.URLError as e:
            if hasattr(e, "code"):
                print(e.code)
            if hasattr(e, "reason"):
                print(e.reason)
    elif type == 2:
        respo = requests.get(Url, headers=head)
        respo.encoding = respo.apparent_encoding
        print(respo.text)
        result = etree.HTML(respo.text).xpath("//a[@class='dynamic-link']/@href")

        # result = etree.HTML(html).xpath("//a[@class='dynamic-link']/@href")

    return result


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
                with open("/data/luck_url.json", "r", encoding="utf-8") as da:
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
    # web.close()


if __name__ == '__main__':
    jihe_url = "https://message.bilibili.com/?spm_id_from=444.42.0.0#/whisper/mid226257459"
    tuan_url = "https://message.bilibili.com/?spm_id_from=444.42.0.0#/whisper/mygroups/fans221096830"
    with open("/data/luck_url.json", "r", encoding="utf-8") as da:
        js = json.load(da)
    web.execute_script(f"window.open()")
    web.switch_to.window(web.window_handles[-1])
    res = Get_luck_list(jihe_url,1)
    '''li = ["https://www.bilibili.com/read/cv23643406","https://www.bilibili.com/read/cv23577393","https://www.bilibili.com/read/cv23493590"]
    for i,f in enumerate(li):
        res3 = Get_Luck_Url_html(li[i],1)
        for j,o in enumerate(res3):
            res.append(res3[j])'''

    # res = Get_Luck_Url_html(url_list,1)
    res2 = Get_luck_list(tuan_url,2)
    for i,url in enumerate(res2):
        res.append(res2[i])

    # res = list(set(res))
    # res.sort(key=res.index)

    # 排除支援团特殊抽奖链接
    for i, res_to in enumerate(res):
        if "?" in res[i]:
            head, sep, tail = res[i].partition("?")
            res[i] = head

    # sortes函数去重列表中的数据
    res = sorted(set(res), key=res.index)
    # 去掉非抽奖链接
    for i, res_to in enumerate(res):
        if "tab" in res_to:
            res.pop(i)
    # 换成新链接地址
    for i, res_to in enumerate(res):
        res[i] = res_to.replace("https://t.bilibili.com/", "https://www.bilibili.com/opus/")

    # 获取所有抽奖链接
    # res = Get_luck_url(html)
    # 遍历执行抽奖
    # web.execute_script(f"window.open('www.baidu.com')")
    # web.switch_to.window(web.window_handles[-1])
    # 跑应援团链接
    for i,url in enumerate(res):
        # print(js[tuan_url][0])
        if res[i] in js:
            print("-"*100 + f"\n{i}" + "\n" + res[i] + "\n跑过了，不跑！\n")
        else:
            print("-"*100 + f"\n{i}" + "\n" + res[i] + "\n没有跑过，来跑一遍！\n")
            success = 0
            success = Go_url(res[i])
            dic_u = {res[i]:success}
            js.update(dic_u)
            with open("/data/luck_url.json", "w", encoding="utf-8") as da:
                json.dump(js, da, ensure_ascii=False, indent=2)





    '''if url_list in js and js[url_list]["success"] == 0:
        for i, u in enumerate(js[url_list]["url_list"][0]):
            # if "tab" in u:
            #     print("这是无效的" + u)
            #     continue
            # u = u.replace("https://t.bilibili.com/", "https://www.bilibili.com/opus/")
            # 更改，修正
            # if js["https://www.bilibili.com/read/cv23542798"]["url_list"][i] == "https://t.bilibili.com/784036474706198534":
            if js[url_list]["url_list"][0][u] == 0:
                print("-" * 100 + "\n" + f"{i}" + "\n没有操作过，运行抽奖：")
                print("现在跑这个链接：" + u)
                # 跑一次
                success = Go_url(u)
                js[url_list]["url_list"][0][u] = success
                # print("成功后，js[url_list][i][u]=1"+"\n"+'-'*100)
                # 数据写入json
                with open("log.json", "w", encoding="utf-8") as da:
                    json.dump(js, da, ensure_ascii=False, indent=2)
            else:
                print("-" * 100 + "\n" + f"{i}" + "\n已经操作过！跳过这个抽奖！\n" + u + "\n" + "-" * 100)
            # js["https://www.bilibili.com/read/cv23542798"]["url_list"][i] = {u:"0"}
    elif url_list in js and js[url_list]["success"] == 0:
        print("-" * 100 + "\n操作过这个集合,跳过这个集合！\n" + url_list + "\n" + "-" * 100)
    elif url_list not in js:
        print("-" * 100 + "\n没有操作过这个集合，去抽奖")
        # 跑一次
        dicc = {}
        listt = []
        dicc2 = {}
        dicc3 = {}
        dicc4 = {url_list: dicc2}
        dicc6 = {"url_list": listt}
        dicc5 = {"success": 0}

        for i, j in enumerate(res):
            dicc3.update({res[i]: 0})
        listt.append(dicc3)
        dicc2.update(dicc6)
        dicc2.update(dicc5)
        dicc.update(dicc4)
        js.update(dicc)
        # 数据写入json
        with open("log.json", "w", encoding="utf-8") as da:
            json.dump(js, da, ensure_ascii=False, indent=2)

        for i, u in enumerate(js[url_list]["url_list"][0]):
            print(f"{i}\n" + "现在跑这个链接：" + u)
            success = Go_url(u)
            js[url_list]["url_list"][0][u] = success
            # 单条抽奖链接数据写入json
            with open("log.json", "w", encoding="utf-8") as da:
                json.dump(js, da, ensure_ascii=False, indent=2)'''

    '''# 这是好的
    for i , uu in enumerate(res):
        uu = uu.replace("https://t.bilibili.com/", "https://www.bilibili.com/opus/")
        if "tab" in uu:
            print("这是无效的"+uu)
            continue
        print(i,uu)
        Go_url(uu)
        print(uu + "处理完成\n")'''

    '''for urls in res:
        urls = urls.replace("https://t.bilibili.com/", "https://www.bilibili.com/opus/")
        if "tab" in urls:
            print("这是无效的"+urls)
            continue
        print(urls+"\n")
        Go_url(urls)
        print(urls+"处理完成\n")'''

    web.quit()
    # print(urls)
    # Go_url("https://www.bilibili.com/opus/772788006861930497")
    # 预约：https://www.bilibili.com/opus/791460707905306643   非官方：https://www.bilibili.com/opus/791828382901862421
    # method.base.lucky_method("https://t.bilibili.com/772788006861930497",web)




