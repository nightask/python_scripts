import requests
import re
import os

# 获取网站图片
if __name__ == '__main__':

    if not os.path.exists("./images"):
        os.mkdir("./images")

    vprotocal = "https:"
    url = vprotocal + "//www.pinduoduo.com/"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'}
    pagetext = requests.get(url, headers=headers).text

    # 用正则表达式匹配图片地址
    ex = '<img class.*?src="(.*?)".*?>'
    images = re.findall(ex, pagetext, re.S)
    print(images)

    for image_src in images:
        if image_src[:2] == "//":
            image_src = vprotocal + image_src
        # 取得的图片文件是二进制格式，所以要用.content取得其内容
        image = requests.get(image_src, headers=headers).content
        image_path = "./images/" + image_src.split('/')[-1]

        with open(image_path, "wb") as fp:
            fp.write(image)

    print("end")

