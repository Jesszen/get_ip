#encoding:utf-8
import threading
import requests
import redis
import random
import time
from usa_pc import USA

def test_ip(ip):
    headers = {
        'Referer': 'http://www.baudi.com/',
        'User-Agent': random.choice(USA)
    }
    try:
        proxies = {"http":ip}
        url_list = ["http://www.baidu.com/","https://v.qq.com/","https://www.tmall.com/","http://www.sina.com.cn/"]
        test_url = random.choice(url_list)
        # timeout 为访问超时设置，我设置为3秒，根据自己喜好更改
        response = requests.get(test_url, headers=headers, proxies=proxies, timeout=3)
        status = response.status_code
        if status == 200:
            print("—————biubiu 连接成功：{}可用——————".format(ip))
            key = ip.split("/")[-1]
            # times 用来记录改ip成功获取网页次数，
            r.hset("hash_kuai", key, {"ip": ip, "times": 1})
        # 有时网站会应为对user-agent做限制，导致403错误，并不代表ip不可用
        elif status ==403:
            print("##########dudu 连接403：{}回炉重造############".format(ip))
            r.lpush("kuai_ip", ip)
        else :
            print("***********dudu 连接失败：{}果断弃了************".format(ip))
    except Exception as e:
        print("**********dudu 连接失败：{}果断弃了****************".format(ip))
        pass

if __name__ == '__main__':
    r = redis.from_url("redis://:密码@localhost:6666/0", decode_responses=True)
    while True:
        ip = r.rpop("kuai_ip")
        t1 =threading.Thread(target=test_ip,args=[ip])
        t1.start()
        # 每隔0.3秒增加一个线程，加快验证，时间长短可以根据自己喜好调整
        time.sleep(0.3)

