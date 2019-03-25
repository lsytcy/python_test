import gevent
from gevent import monkey;monkey.patch_all()
from threading import Thread
from time import time
from bs4 import BeautifulSoup
import requests


t1 = time()

urls = [
    "https://movie.douban.com/top250?start={}&filter=".format(i)
    for i in range(0,226,25)
    ]

def job(url):
    r = requests.get(url)
    content = r.text
    soup = BeautifulSoup(content, 'html.parser')
    item = soup.select(".item")
    for i in item:
        print(i.select(".title")[0].text)

works = [gevent.spawn(job,url) for url in urls]
gevent.joinall(works)

print('耗时：',time() - t1)