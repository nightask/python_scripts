import requests
import json

if __name__ == '__main__':

    vprotocal = "https://"
    url = vprotocal + "fanyi.baidu.com/sug"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'}
    queryword = input("请录入需要翻译的词语：")
    parm = {'kw': queryword}
    res = requests.post(url, data=parm, headers=headers)
    dict_obj = json.loads(res.text, encoding='utf-8')
    # print(len(dict_obj['data']))
    # print(dict_obj['data'])

    # 本程序只选择第一个翻译结果
    if len(dict_obj['data']):
        res1 = dict_obj['data'][0]['v']
        print('翻译出的内容：', res1)
    else:
        print('未能翻译成功!')
