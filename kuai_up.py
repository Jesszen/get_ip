#encoding:utf-8
from bs4 import BeautifulSoup
import requests
import redis
import random
import time
from usa_pc import USA

def get_ip(i):
    headers1 = {
        'Referer': 'http://www.kuaidaili.com/free/inha/',
        'User-Agent': random.choice(USA)
    }
    url= 'http://www.kuaidaili.com/free/inha/'+str(i)+'/'
    response = requests.get(url,headers=headers1)
    soup = BeautifulSoup(response.text,"lxml")
    trs= soup.find("table",class_="table table-bordered table-striped").find_all("tr")
    for tr in trs[1:]:
        ip = tr.find_all("td")[0].get_text()
        port = tr.find_all("td")[1].get_text()
        proxy = "http://"+ip+":"+port
        r.lpush("kuai_ip",proxy)
    time.sleep(random.randint(3, 4))

if __name__ == '__main__':
    r = redis.from_url("redis://:lj910226@localhost:6666/0",decode_responses=True)  #  decode_responses=True 传入为str否则为字节
    for i in range(1, 101):
        get_ip(i)