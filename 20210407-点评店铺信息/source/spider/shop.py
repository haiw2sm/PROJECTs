# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 21:20:10 2021

@author: w2hi
"""

from requests_html import HTMLSession, user_agent
import time
import random
import sys
import pandas as pd
# 全局变量

from source.module.confusion.css import ParseEncodedStr
try:
    from settings import *
except Exception as e:
    raise e

session = HTMLSession()
headers = {
    "Cookie": Cookie,
    "Host": "www.dianping.com",
    "Upgrade-Insecure-Requests": "1",
    'User-Agent': user_agent('random')
}

class DianPing(ParseEncodedStr):
    """docstring for DianPing"""
    def __init__(self, DATA_DIR, city):
        super(DianPing, self).__init__(DATA_DIR, )
        self.DATA_DIR = DATA_DIR
        self.city = city

    # 获取随机代理
    def get_random_proxy(self):
        resp = session.get('http://127.0.0.1:5555/random')
        proxy = resp.html.text
        try:
            resp2 = session.get('http://www.dianping.com/',
                                proxies={'http': proxy},
                                timeout=3,
                                headers=headers
                                )
        except Exception as e:
            print(proxy, '\t\t失效')
            self.get_random_proxy()
        else:
            if resp2.status_code == 200:
                return proxy
            else:
                self.get_random_proxy()


    def get_by_city(self):
        for i in range(25, 210):
            # proxy = self.get_random_proxy()
            baseUri = f'http://www.dianping.com/{self.city}/ch10/p{i}'
            print('=' * 10, '第%s页' % i, '=' * 10)
            resp = session.get(baseUri, headers=headers)
            # print(resp.html.html)
            nodes = resp.html.find("#shop-all-list > ul > li")  ## set
            print(len(nodes))
            # print(nodes)
            result = []
            if nodes:
                for node in nodes:
                    each = {}
                    linkElem = node.find('div.txt > div.tit > a', first=True)
                    # 店铺链接
                    each['dpurl'] = linkElem.attrs['href']
                    # 店铺标题
                    each['dptitle'] = linkElem.attrs["title"]
                    
                    # 店铺总分
                    try:
                        each['dpstar'] = node.find(selector='div.star_score',first=True).text
                    except:
                        each['dpstar'] = '-'
                    
                    # 评论人数
                    try:
                        plnumStr = node.find(selector='a.review-num > b', first=True).text
                        each['plnum'] = self.parse(rawStr=plnumStr, className='shopNum')
                    except:
                        each['plnum'] = '-'
                    print(each['plnum'], end=',')


                    
                    # 人均消费
                    try:
                        rjcostStr = node.find(selector='a.mean-price > b', first=True).text  #'￥11\n\ueadd'
                        each['rjcost'] = rjcostStr[0] + self.parse(rawStr=rjcostStr[1:], className='shopNum')
                    except:
                        each['rjcost'] = '-'
                    print(each['rjcost'], end=',')
                    

                    # 口味评分
                    try:
                        kwscoreStr = node.find(selector='span.comment-list > span > b', first=True).text
                        each['kwscore'] = self.parse(rawStr=kwscoreStr, className='shopNum')
                    except:
                        each['kwscore'] = ''
                    print(each['kwscore'], end=',')
                    
                    
                    # 环境评分
                    try:
                        hjscoreStr = node.find(selector='span.comment-list > span:nth-child(2) > b', first=True).text
                        each['hjscore'] = self.parse(rawStr=hjscoreStr, className='shopNum')
                    except:
                        each['hjscore'] = '-'
                    print(each['hjscore'], end=',')

                    # 服务评分
                    try:
                        fwscoreStr = node.find(selector='span.comment-list > span:nth-child(3) > b', first=True).text
                        each['fwscore'] = self.parse(rawStr=fwscoreStr, className='shopNum')
                    except:
                        each['fwscore'] = '-'
                    print(each['fwscore'])
                    # result.append(each)


                    with open(os.path.join(self.DATA_DIR, 'result2.csv'), 'a+', encoding='utf-8') as f:
                        line = ','.join(list(each.values())) + '\n'
                        f.write(line)
                    # print(each)

                time.sleep(2 + random.random() * 5)

    def run(self):
        self.get_by_city()
        print('数据抓取完成')


if __name__ == '__main__':
    city = sys.argv[1]
    dp = DianPing(DATA_DIR=DATA_DIR, city=city)
    dp.run(city)
