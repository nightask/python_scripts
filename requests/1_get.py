import requests

# 利用get()函数获取网页的内容
if __name__ == '__main__':

    vprotocal = "https://"
    url = vprotocal + "www.baidu.com/s"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'}
    queryword = input("请录入查询内容：")

    # 将该页面给出的查询关键字标识名为q，形如： ***.***.***/s?q=XXX
    # 传给网页的参数名字要与查询关键字标识名一致
    parm = {'q': queryword}
    res = requests.get(url, params=parm, headers=headers)
    txt = res.text

    with open("./test1.html", "w", encoding="utf-8") as fs:
        fs.write(txt)

    print("程序运行完成")