# 获取所有解析接口
import re

import requests


# 获取每日励志精句
# def get_message():
#     r = get("http://open.iciba.com/dsapi/")
#     note = r.json()['note']
#     content = r.json()['content']
#     tts = r.json()['tts']
#     fenxiang_img = r.json()['fenxiang_img']
#     return note, content, tts, fenxiang_img


def getjiekou(url):
    # url = "http://www.qmaile.com/"
    r = requests.get(url)
    r.encoding = r.apparent_encoding
    url_content = r.text
    # print(r.raise_for_status())
    # print(r.status_code)
    # print(url_content)
    # 数据提取
    code_re = re.compile('<option value="(.*?)" selected')
    locaction_content = re.findall(code_re, url_content)  # find_all函数选择所有匹配到的结果
    return locaction_content
