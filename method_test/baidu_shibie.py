# -*- codeing = utf-8 -*-
# @File:baidu_shibie.py
# @Software:PyCharm
# @Author:keven
# @Time:2023/5/5 11:57
import base64
import urllib
import requests


# 获取token,用自己的client_id和client_secret
def get_token():
    url = "https://aip.baidubce.com/oauth/2.0/token?client_id=QB9HA7ALar3z1l4d1jfDuvu7&client_secret=bS2cLc0gz0QNV1Uz2ASs8w9My5B6bGSv&grant_type=client_credentials"

    payload = ""
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.json()["access_token"]

# 调用接口识别文字
def main(payload):
    url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate?access_token=" + get_token()

    # image 可以通过 get_file_content_as_base64("C:\fakepath\code.png",True) 方法获取
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json'
    }
    # 可以查看各个参数的定义https://ai.baidu.com/ai-doc/OCR/tk3h7y2aq
    payloadd = {
        "image":payload,
        "detect_direction":"true",
        "probability":"true"
    }
    response = requests.request("POST", url, headers=headers, data=payloadd)

    print("-"*100 + "\n这是百度接口返回识别出来的文字和位置：" + response.text + "\n准确度还是不够，弃用\n" + "-"*100)
    return response.text


def get_file_content_as_base64(path, urlencoded=False):
    """
    获取文件base64编码
    :param path: 文件路径
    :param urlencoded: 是否对结果进行urlencoded
    :return: base64编码信息
    """
    with open(path, "rb") as f:
        content = base64.b64encode(f.read()).decode("utf8")
        if urlencoded:
            content = urllib.parse.quote_plus(content)
    return content


# if __name__ == '__main__':
#     main(Image.open("code.png"))
