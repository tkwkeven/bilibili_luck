# -*- codeing = utf-8 -*-
# @File:ins.py
# @Software:PyCharm
# @Author:keven
# @Time:2023/5/8 20:51
import json


def inst(ss):
    aa = ss
    e = ['https://www.bilibili.com/opus/784036474706198534', 'https://www.bilibili.com/opus/783917469728243860', 'https://www.bilibili.com/opus/788834253785792594', 'https://www.bilibili.com/opus/790229319347601414', 'https://www.bilibili.com/opus/791433490738446374', 'https://www.bilibili.com/opus/791810498672721921', 'https://www.bilibili.com/opus/791791463381860385', 'https://www.bilibili.com/opus/792119057671258132', 'https://www.bilibili.com/opus/792084388745576516', 'https://www.bilibili.com/opus/781748721720229926', 'https://www.bilibili.com/opus/780158673261428745', 'https://www.bilibili.com/opus/782855045144117272', 'https://www.bilibili.com/opus/782467381381300264', 'https://www.bilibili.com/opus/783992670309580838', 'https://www.bilibili.com/opus/783216363584880660', 'https://www.bilibili.com/opus/783589067938856992', 'https://www.bilibili.com/opus/787625186145861656', 'https://www.bilibili.com/opus/788819221400256529', 'https://www.bilibili.com/opus/788802801753915392', 'https://www.bilibili.com/opus/788006291519832096', 'https://www.bilibili.com/opus/787965489286479872', 'https://www.bilibili.com/opus/788423251225214983', 'https://www.bilibili.com/opus/789502696739569670', 'https://www.bilibili.com/opus/789483734456860694', 'https://www.bilibili.com/opus/789852427378491393', 'https://www.bilibili.com/opus/789484340091289684', 'https://www.bilibili.com/opus/790597028635738438', 'https://www.bilibili.com/opus/790597002911023155', 'https://www.bilibili.com/opus/789155324121579520', 'https://www.bilibili.com/opus/782520033395867651', 'https://www.bilibili.com/opus/791353286504480793', 'https://www.bilibili.com/opus/790433119799869460', 'https://www.bilibili.com/opus/789909640639938625', 'https://www.bilibili.com/opus/789215792970334213', 'https://www.bilibili.com/opus/792189374925111347', 'https://www.bilibili.com/opus/792526289289347088', 'https://www.bilibili.com/opus/782049120298729475', 'https://www.bilibili.com/opus/782882975339511860', 'https://www.bilibili.com/opus/785448234727243784', 'https://www.bilibili.com/opus/788118716569092136', 'https://www.bilibili.com/opus/786861682720768050', 'https://www.bilibili.com/opus/786564926210572344', 'https://www.bilibili.com/opus/786529359586394131', 'https://www.bilibili.com/opus/786224270892072979', 'https://www.bilibili.com/opus/785878899685851137', 'https://www.bilibili.com/opus/785830005805416472', 'https://www.bilibili.com/opus/785741611081400338', 'https://www.bilibili.com/opus/785729761244610564', 'https://www.bilibili.com/opus/785543746234089512', 'https://www.bilibili.com/opus/785508407244226581', 'https://www.bilibili.com/opus/787625551260024872', 'https://www.bilibili.com/opus/787609694239719430', 'https://www.bilibili.com/opus/787606838031941688', 'https://www.bilibili.com/opus/787603977641394224', 'https://www.bilibili.com/opus/787258975801311253', 'https://www.bilibili.com/opus/787257682971066387', 'https://www.bilibili.com/opus/787238304081772544', 'https://www.bilibili.com/opus/786991407884664885', 'https://www.bilibili.com/opus/786980172296355889', 'https://www.bilibili.com/opus/786917667634151426', 'https://www.bilibili.com/opus/786917444250763264', 'https://www.bilibili.com/opus/786916898820325381', 'https://www.bilibili.com/opus/786911225183207475', 'https://www.bilibili.com/opus/786885807568846881', 'https://www.bilibili.com/opus/786883440985243653', 'https://www.bilibili.com/opus/786878677922086928', 'https://www.bilibili.com/opus/786877492464975876', 'https://www.bilibili.com/opus/786877045815640104', 'https://www.bilibili.com/opus/788072760379179008', 'https://www.bilibili.com/opus/786988938278469685', 'https://www.bilibili.com/opus/786498938344570885', 'https://www.bilibili.com/opus/786130520348033106', 'https://www.bilibili.com/opus/785871916096290864', 'https://www.bilibili.com/opus/785841988764172288', 'https://www.bilibili.com/opus/785825337175965737', 'https://www.bilibili.com/opus/785818198916202552', 'https://www.bilibili.com/opus/782949487165309044', 'https://www.bilibili.com/opus/786922215964672003', 'https://www.bilibili.com/opus/792123503005401095', 'https://www.bilibili.com/opus/792075227579285542', 'https://www.bilibili.com/opus/791791205686968321', 'https://www.bilibili.com/opus/791775816768815127', 'https://www.bilibili.com/opus/791681971781632025', 'https://www.bilibili.com/opus/789973193267871748', 'https://www.bilibili.com/opus/789104944158343172', 'https://www.bilibili.com/opus/788810025930850325', 'https://www.bilibili.com/opus/788774287463940102', 'https://www.bilibili.com/opus/788769404133310483', 'https://www.bilibili.com/opus/788749170542379030', 'https://www.bilibili.com/opus/791676285196697621', 'https://www.bilibili.com/opus/788326300899082272', 'https://www.bilibili.com/opus/790601005773357079', 'https://www.bilibili.com/opus/791673613729136647', 'https://www.bilibili.com/opus/787303579020951591', 'https://www.bilibili.com/opus/792210540520800296', 'https://www.bilibili.com/opus/791795045380390978', 'https://www.bilibili.com/opus/791783917120126984', 'https://www.bilibili.com/opus/789930488367153157', 'https://www.bilibili.com/opus/789112808224587831', 'https://www.bilibili.com/opus/788716752083091480', 'https://www.bilibili.com/opus/788028466421301265', 'https://www.bilibili.com/opus/787312052951580696', 'https://www.bilibili.com/opus/786995200369098771', 'https://www.bilibili.com/opus/786980674764537927', 'https://www.bilibili.com/opus/786964152067293189', 'https://www.bilibili.com/opus/786949029430820873', 'https://www.bilibili.com/opus/786943016532181001', 'https://www.bilibili.com/opus/786554193099882505', 'https://www.bilibili.com/opus/790596981435138214', 'https://www.bilibili.com/opus/790225896213577928', 'https://www.bilibili.com/opus/788745850531610624', 'https://www.bilibili.com/opus/789847861829304341', 'https://www.bilibili.com/opus/786886108196634710', 'https://www.bilibili.com/opus/791753495821680645']

    aa = "aa"
    bb = "bb"
    tt = {"d": "3"}
    intr = {"success":"0"}
    # print(len(e["https://www.bilibili.com/read/cv23542798"]))

    er = "https://www.bilibili.com/opus/784036474706198534?spm_id_from=333.999.0.0"
    if "?" in er:
        head, sep, tail = er.partition("?")
        print(head)

    with open("log.json", "r", encoding="utf-8") as da:
        js = json.load(da)
    print(js["url_list"])

    if "https://www.bilibili.com/read/cv23542798" in js and js["https://www.bilibili.com/read/cv23542798"]["success"] == "0":
        # print("是")
        fff = []
        for i, u in enumerate(js["https://www.bilibili.com/read/cv23542798"]["url_list"]):
            # print(u)
            # print(js["https://www.bilibili.com/read/cv23542798"]["url_list"][i])
            # if js["https://www.bilibili.com/read/cv23542798"]["url_list"][i] == "https://t.bilibili.com/784036474706198534":
            for o in u:
                ol = o
            old = js["https://www.bilibili.com/read/cv23542798"]["url_list"][i]
            ooo = old
            u[e[i]] = u.pop(ol)
            # print(e[i])
            # print(js["https://www.bilibili.com/read/cv23542798"]["url_list"][i])

            # new = e[i]




            '''if ("https://t.bilibili.com/784036474706198534" in u) and u["https://t.bilibili.com/784036474706198534"] == "0":
                print("没有操作过，运行抽奖：")
                # u = u[].replace("https://t.bilibili.com/", "https://www.bilibili.com/opus/")
                for c in u:
                    a = c
                    # c = c.replace("https://t.bilibili.com/", "https://www.bilibili.com/opus/")
                    print(a)
                    # print(c)
                    u[e[i]] = u.pop[c]
                    print(u)

            else:
                print("已经操作过！跳过这个抽奖！")'''
        # print(fff)
        # js["https://www.bilibili.com/read/cv23542798"]["url_list"] = fff
        # print(js["https://www.bilibili.com/read/cv23542798"]["url_list"])
            # js["https://www.bilibili.com/read/cv23542798"]["url_list"][i] = {u:"0"}
    elif js["https://www.bilibili.com/read/cv23542798"]["success"] == "1":
        print("操作过这个集合,跳过这个链接！")
    elif "https://www.bilibili.com/read/cv23542798" not in js:
        print("没有操作过这个集合，去抽奖")

    # sss = {"aa":[{"bb":"1"},{"vv":"2"}]}
    # for i in sss:
    #     print(i)






    # js.update(intr)
    # print(js)

    # with open("log.json", "w", encoding="utf-8") as da:
    #     json.dump(js, da, ensure_ascii=False, indent=2)
    # print()

    return aa

if __name__ == '__main__':
    inst("ss")