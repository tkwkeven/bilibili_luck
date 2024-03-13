# -*- codeing = utf-8 -*-
# @File:Bilibili_lucky_main.py
# @Software:PyCharm
# @Author:keven
# @Time:2023/5/18 11:20

#python文件下会自动调用当前项目下其他包；避免mac通过终端执行.py时报错找不到文件夹；
# 工作目录不一样：
# 通过pycharm运行，工作目录就是项目位置，pycharm自己封装的一系列操作，拿得到其他包；
# 通过终端执行，工作目录在执行文件位置，系统拿不到同项目下其他包，就会报错
import sys

import time
import pytest
from method import conftest
sys.path.append('../')
import json
from method.Bilibili_lucky_Parent_Class import Bilibili_lucky_Parent_Class as tbl_class
from method.Get_lucky_list import Get_luck_list as gll
from method.Link_Processing import Link_Processing as lp


class Bilibili_lucky_main(tbl_class):
    def bilibili_lucky_main(self):
        gll_class = gll()
        lp_class = lp()
        res = []

        # jihe_url = "https://message.bilibili.com/?spm_id_from=444.42.0.0#/whisper/mid226257459"   #用专栏页面代替
        tuan_url = "https://message.bilibili.com/?spm_id_from=444.42.0.0#/whisper/mygroups/fans221096830"
        zhuanlan_url_00 = "https://space.bilibili.com/226257459/article"
        zhuanlan_url = "https://space.bilibili.com/3493086911007529/article"
        zhuanlan_url_2 = "https://space.bilibili.com/5536630/article"
        # zhuanlan_url_3 = "https://space.bilibili.com/99439379/article" #链接无效
        zhuanlan_url_4 = "https://space.bilibili.com/200824032/article"
        # zhuanlan_url_5 = "https://space.bilibili.com/384876770/article"   #抽奖时间到达才汇集，没用
        zhuanlan_url_6 = "https://space.bilibili.com/492426375/article"
        # zhuanlan_url_7 = "https://space.bilibili.com/280579777/article"    #主页已经没有抽奖链接
        zhuanlan_url_8 = "https://space.bilibili.com/280025263/article"
        zhuanlan_url_9 = "https://space.bilibili.com/1905702375/article"
        # zhuanlan_url_10 = "https://space.bilibili.com/1284836532/article"  #链接无效


        # res = gll_class.get_luck_list(jihe_url, 1)    #用专栏页面代替
        res2 = gll_class.get_luck_list(tuan_url, 2)
        res3 = gll_class.get_luck_list(zhuanlan_url, 3)
        res00 = gll_class.get_luck_list(zhuanlan_url_00,3)
        res3_2 = gll_class.get_luck_list(zhuanlan_url_2, 3)
        # res3_3 = gll_class.get_luck_list(zhuanlan_url_3, 3)
        res3_4 = gll_class.get_luck_list(zhuanlan_url_4, 3)
        # res3_5 = gll_class.get_luck_list(zhuanlan_url_5, 3)   #抽奖时间到达才汇集，没用
        res3_6 = gll_class.get_luck_list(zhuanlan_url_6, 3)
        # res3_7 = gll_class.get_luck_list(zhuanlan_url_7,3)    #主页已经没有抽奖链接
        res3_8 = gll_class.get_luck_list(zhuanlan_url_8,3)
        res3_9 = gll_class.get_luck_list(zhuanlan_url_9,3)
        # res3_10 = gll_class.get_luck_list(zhuanlan_url_10,3)


        for i, url in enumerate(res2):  # 全部放入一个列表里面
            res.append(res2[i])
        for i, url in enumerate(res3):  # 全部放入一个列表里面
            res.append(res3[i])
        for i, url in enumerate(res00):  # 全部放入一个列表里面
            res.append(res00[i])
        for i, url in enumerate(res3_2):  # 全部放入一个列表里面
            res.append(res3_2[i])
        # for i, url in enumerate(res3_3):  # 全部放入一个列表里面
        #     res.append(res3_3[i])
        for i, url in enumerate(res3_4):  # 全部放入一个列表里面
            res.append(res3_4[i])
        # for i, url in enumerate(res3_5):  # 全部放入一个列表里面#抽奖时间到达才汇集，没用
        #     res.append(res3_5[i])
        for i, url in enumerate(res3_6):  # 全部放入一个列表里面
            res.append(res3_6[i])
        # for i, url in enumerate(res3_7):  # 全部放入一个列表里面
        #     res.append(res3_7[i])
        for i, url in enumerate(res3_8):  # 全部放入一个列表里面
            res.append(res3_8[i])
        for i, url in enumerate(res3_9):  # 全部放入一个列表里面
            res.append(res3_9[i])
        # for i, url in enumerate(res3_10):
        #     res.append(res3_10[i])

        # 全部放一个list统一处理
        res = lp_class.link_processing(res=res)

        for i, url in enumerate(res):
            if res[i] in tbl_class.js:
                print("-" * 100 + f"\n{i}" + "\n" + res[i] + "\n跑过了，不跑！\n")
            else:
                print("-" * 100 + f"\n{i}" + "\n" + res[i] + "\n没有跑过，来跑一遍！")
                # success = conftest.success
                tbl_class.web.get(res[i])
                time.sleep(1.5)

                # success = gu_class.go_url(res[i])
                # 判断分类，走不同的处理逻辑
                if len(tbl_class.web.find_elements("css selector","span[class='opus-text-rich-hl lottery']")) > 0 :
                    pytest.main(["-s","-v","method/test_Go_url.py::Test_Go_url::test_go_url_GF"])
                elif len(tbl_class.web.find_elements("css selector","span[class='bili-dyn-card-reserve__lottery__text'],span[class='bili-dyn-upower-lottery__lottery__text']")) > 0:
                    pytest.main(["-s","-v","method/test_Go_url.py::Test_Go_url::test_go_url_YY"])
                elif len(tbl_class.web.find_elements("css selector", "div[class='side-toolbar__action forward']")) > 0:
                    pytest.main(["-s", "-v","method/test_Go_url.py::Test_Go_url::test_go_url_FGF_new"])
                else:
                    pytest.main(["-s", "-v","method/test_Go_url.py::Test_Go_url::test_go_url_FGF_old"])

                dic_u = {res[i]: 1}
                tbl_class.js.update(dic_u)
                with open(tbl_class.data_local, "w", encoding="utf-8") as da:
                    json.dump(tbl_class.js, da, ensure_ascii=False, indent=2)


    def Weibo_lucky_main(self):
        gll_class = gll()
        lp_class = lp()

        jihe_url = "https://weibo.com/u/6196818433"
        jihe_url2 = "https://weibo.com/u/5659513217"
        # jihe_url3 = "https://weibo.com/u/5767584759"


        res4 = gll_class.get_luck_list(jihe_url, 4)
        res4_2 = gll_class.get_luck_list(jihe_url2, 4)
        # res4_3 = gll_class.get_luck_list(jihe_url3,4)
        # print(res4_3)

        for i, url in enumerate(res4_2):  # 加入其他博主第三种页面抽奖链接
            res4.append(res4_2[i])
        # for i, url in enumerate(res4_3):  # 加入其他博主第三种页面抽奖链接
        #     res4.append(res4_3[i])

        # 放一个list统一处理
        res = lp_class.link_processing(res2=res4)

        for i, url in enumerate(res):
            if res[i] in tbl_class.js:
                print("-" * 100 + f"\n{i}" + "\n" + res[i] + "\n跑过了，不跑！\n")
            else:
                print("-" * 100 + f"\n{i}" + "\n" + res[i] + "\n没有跑过，来跑一遍！")
                success = 0
                tbl_class.web.get(res[i])

                pytest.main(["-s", "-v","method/test_Go_url.py::Test_Go_url::test_go_url_WB"])
                # success = gu_class.go_weibo_url(res[i])

                dic_u = {res[i]: success}
                tbl_class.js.update(dic_u)
                with open(tbl_class.data_local, "w",
                          encoding="utf-8") as da:
                    json.dump(tbl_class.js, da, ensure_ascii=False, indent=2)

    def Xiaohongshu_lucky_main(self):   # 无效，浏览器实例web被检测出是爬虫机器人
        gll_class = gll()
        lp_class = lp()

        jihe_url = "https://www.xiaohongshu.com/user/profile/5f65d0950000000001003001"
        # jihe_url2 = "https://weibo.com/u/6196818433"

        res5 = gll_class.get_luck_list(jihe_url, 4)
        # res4_2 = gll_class.get_luck_list(jihe_url2, 4)

        '''for i, url in enumerate(res4_2):  # 加入其他up第三种页面抽奖链接
            res4.append(res4_2[i])'''

        # res = lp_class.link_processing(res3=res5)

        '''for i, url in enumerate(res):
            if res[i] in tbl_class.js:
                print("-" * 100 + f"\n{i}" + "\n" + res[i] + "\n跑过了，不跑！\n")
            else:
                print("-" * 100 + f"\n{i}" + "\n" + res[i] + "\n没有跑过，来跑一遍！\n")
                success = 0
                success = gu_class.go_weibo_url(res[i])
                dic_u = {res[i]: success}
                tbl_class.js.update(dic_u)
                with open("/Users/bytedance/PycharmProjects/bilibili_luck/data/luck_url.json", "w",
                          encoding="utf-8") as da:
                    json.dump(tbl_class.js, da, ensure_ascii=False, indent=2)'''

if __name__ == '__main__':
    bilibili = Bilibili_lucky_main()



    bilibili.bilibili_lucky_main()
    bilibili.Weibo_lucky_main()

    # bilibili.Xiaohongshu_lucky_main()   #无效，被检测出爬虫机器人--->已经规避检测，可以正常登录浏览，但是网页小红书没有抽奖按钮，无法抽奖

    tbl_class.web.quit()



