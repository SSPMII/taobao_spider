# -*- conding:utf-8 -*-
import requests
import re

def get_html_text(url):
        try:
                r = requests.get(url, timeout=30)
                r.raise_for_status
                r.encoding = r.apparent_encoding
                return r.text
        except:
                print("get出现异常")


def parse_page(ilt, html):
        try:
                title_list = re.findall(r'"raw_title":".*?"', html)
                price_list = re.findall(r'"view_price":"[\d.]*"', html)
                loc_list = re.findall(r'"item_loc":".*?"', html)
                for i in range(len(title_list)):
                        title = eval(title_list[i].split(":")[1])
                        price = eval(price_list[i].split(":")[1])
                        loc = eval(loc_list[i].split(":")[1])
                        ilt.append([title, price, loc])
        except:
                print("parse出现异常")


def print_goods_list(ilt):
        tplt = "{0:4}\t{1:{4}<20}\t{2:<8}\t{3:<12}"
        print(tplt.format("序号", "商品名称", "价格", "产地", chr(12288)))
        count = 0
        for g in ilt:
                count += 1
                print(tplt.format(count, g[0], g[1], g[2], chr(12288)))


def main():
        goods = 'nike'
        deepth = 2
        start_url = 'https://s.taobao.com/search?q=' + goods
        info_list = []
        for i in range(deepth):
                try:
                        url = start_url + '&s=' + str(i*44)
                        html = get_html_text(url)
                        parse_page(info_list, html)
                except:
                        continue
        print_goods_list(info_list)

main()
