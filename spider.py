# -*- coding: utf-8 -*-
import random
import time
import requests
from bs4 import BeautifulSoup
from usa_pc import USA

def test_ip(proxy):
    headers2 = {
        'Referer': 'http://www.runoob.com/python3/python3-tutorial.html',
        'User-Agent': random.choice(USA)
    }
    try:
        proxies = {"http":proxy}
        test_url = "http://www.runoob.com/python3/python3-tutorial.html"
        response = requests.get(test_url, headers=headers2, proxies=proxies, timeout=3)
        return response.status_code
    except :
        pass

def to_text(proxy):
    print("########################biubiu连接成功：{}可用写入中##############################".format(proxy))
    with open("ip_pool.txt","a",encoding="utf-8") as f:
        f.write(proxy+"\n")
        f.close()

def get_ip(i):
    headers1 = {
        'Referer': 'http://www.66ip.cn/1.html',
        'User-Agent': random.choice(USA)
    }
    url= 'http://www.66ip.cn/'+str(i)+'.html'
    response = requests.get(url,headers=headers1)
    soup = BeautifulSoup(response.content.decode("gbk"),"lxml")
    trs= soup.find("div",class_="containerbox boxindex").find_all("tr")
    for tr in trs[1:]:
        ip = tr.find_all("td")[0].get_text()
        port = tr.find_all("td")[1].get_text()
        proxy = "http://"+ip+":"+port
        status = test_ip(proxy)
        if status == 200:
            to_text(proxy)
        else:
            print("########################dudu链接失败：{}不可用割了##############################".format(proxy))
    # time.sleep(random.randint(3, 4))

if __name__ == '__main__':
    for i in range(1, 101):
        get_ip(i)