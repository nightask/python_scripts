import requests
import re
import os
import time

# 自动获取各分页图片

'''
    定义一个获取每个分页中的图片的函数
    param page_url: 每个分页网址
    param reg_str: 正则表达式字符串
'''
def get_onepage_img(page_url, reg_str):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'}
    pagetext = requests.get(url=page_url, headers=headers).text
    images = re.findall(reg_str, pagetext, re.S)
    v_name = time.strftime('%Y%m%d%H%M%S', time.localtime())
    i = 0
    for image_src in images:
        time.sleep(10)  # 等待10s
        image = requests.get(image_src, headers=headers).content
        i += 1
        image_path = "./images2/" + v_name + str(i) + '-' + image_src.split('/')[-1]

        with open(image_path, "wb") as fp:
            fp.write(image)


if __name__ == '__main__':

    if not os.path.exists("./images2"):
        os.mkdir("./images2")

    vprotocal = "https://"
    print("正在获取各页面上的图片，请稍后...")

    for i in range(1, 2):
        if i == 1:
            url = vprotocal + "shanghai.anjuke.com/sale/?q=%E6%96%B0%E6%88%BF&direct=yes"
        else:
            url = vprotocal + "shanghai.anjuke.com/sale/p{}/?q=%E6%96%B0%E6%88%BF&direct=yes".format(i)

        # 用正则表达式匹配图片地址
        ex = '<img .*?src="(.*?)".*?>'
        print(url)
        get_onepage_img(url, ex)

    print("end")

