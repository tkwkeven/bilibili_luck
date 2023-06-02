# -*- codeing = utf-8 -*-
# @File:Link_Processing.py
# @Software:PyCharm
# @Author:keven
# @Time:2023/5/18 11:12
from method.Bilibili_lucky_Parent_Class import Bilibili_lucky_Parent_Class as tbl

class Link_Processing(tbl):
    def link_processing(self,res=[],res2=[],res3=[],res4=[]):

        # 加上微博链接
        for i, url in enumerate(res2):
            res.append(res2[i])


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
            # 去掉非抽奖链接
            if "read" in res_to:
                res.pop(i)
            # 去掉微博无效链接
            if "lottery" in res_to:
                res.pop(i)
            # 去掉微博话题链接
            if "q=" in res_to:
                res.pop(i)
            # 去掉微博搜索链接
            if "s.weibo" in res_to:
                res.pop(i)

        # 换成新链接地址
        for i, res_to in enumerate(res):
            res[i] = res_to.replace("https://t.bilibili.com/", "https://www.bilibili.com/opus/")


        '''# 去掉无效链接
        for i,res_to in enumerate(res):
            if "lottery" in res_to:
                res.pop(i)'''

        return res