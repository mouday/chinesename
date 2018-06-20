# -*- coding: utf-8 -*-

# @File    : spider.py
# @Date    : 2018-06-20
# @Author  : Peng Shiyu

# 古诗文网爬虫，获取诗文标题和内容

import requests
import json
from  scrapy.selector import Selector
from urllib.request import urljoin


# 获取页面诗经列表
def get_list(url):
    base_url = "https://so.gushiwen.org/"

    response = requests.get(url)

    sel = Selector(response)

    links = sel.css(".typecont a::attr(href)").extract()

    links = [urljoin(base_url, url) for url in links]

    return links


# 获取详细页面内容
def get_detail(url):
    response = requests.get(url)

    sel = Selector(response)

    title = sel.css(".sons h1::text").extract_first("").strip()
    try:
        body = sel.css(".contson")[0].xpath("string(.)").extract_first("").strip()
    except Exception as e:
        body = ""
        print(e)

    return {
        "title": title,
        "body": body,
        "link": url
    }

# 保存
def save_json(dct):
    with open("gushiwen.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(dct, ensure_ascii=False, indent="\t"))



if __name__ == '__main__':

    # 连接列表
    urls = {
        "诗经": "https://so.gushiwen.org/gushi/shijing.aspx",
        "楚辞": "https://so.gushiwen.org/gushi/chuci.aspx",
    }

    dct = {}

    for key, value in urls.items():
        links = get_list(value)
        lst = []
        for link in links:
            print("get link: %s"% link)
            lst.append(get_detail(link))
        dct[key]= lst

    save_json(dct)
