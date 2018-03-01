# -*- coding: utf-8 -*-
import urllib.request
import urllib.error
import http.client
import re
import time
import random
import os

# 打开文件并下载内容
def download_stock_data_by_open(num):
    stock_total = []  # stock_total：所有页面的股票数据   stock_page：某页的股票数据
    url = "http://quote.stockstar.com/stock/ranklist_a_3_1_" + str(num) + ".html"
    try:
        response = urllib.request.urlopen(url)  # type: http.client.HTTPResponse
    except urllib.error.HTTPError as e:
        print(e.code)
    except urllib.error.URLError as e:
        print(e.reason)
    # print(response.read().decode("gbk"))
    content = response.read().decode("gbk")
    # 关闭
    response.close()
    pattern = re.compile('<tbody[\s\S]*</tbody>')
    body = re.findall(pattern, str(content))
    # print(body)
    pattern = re.compile('>(.*?)<')
    stock_page = re.findall(pattern, body[0])
    # print(stock_page)
    stock_total.extend(stock_page)
    for data in stock_total:
        if data == '':
            stock_total.remove(data)
    # 判断stock_total中是否还存在'',如果存在继续remove,测试下来第一次remove不能完全
    while '' in stock_total:
        for data in stock_total:
            if data == '':
                stock_total.remove(data)
    return stock_total


# 写入数据
def stock_data_write_file(filename):
    # 判断文件是否存在,不存在就创建
    if not os.path.exists(filename):
        # 创建文件空文件
        '''
            执行下面代码会报错：
            AttributeError: 'module' object has no attribute 'mknod'
            追其原因是因为windows文件系统与linux文件系统不同，没有node的概念，所以会报错。
            我们在使用追加打开方式的时候，python会自动创建文件 open(filename,'a')
        '''
        # os.mknod(filename)
        # open('f.txt','w')    # r只读，w可写，a追加
        open(filename, 'a')
    # 打开文件,并且给于写的权限,encoding="utf-8" 防止写入的中文出现乱码
    fos = open(filename, 'w', encoding="utf-8")
    title = '代码\t简称\t最新价\t涨跌幅\t涨跌额\t5分钟涨幅\t成交量(手)'
    fos.write(title + '\n')
    # 获取股票数据
    for page in range(1, 9):
        # print("page:" + str(page))
        stock_data = download_stock_data_by_open(page)
        # range(start,end,scan)
        # scan：每次跳跃的间距，默认为1。例如：range(0,5,2) 输出[0,2,4]
        for i in range(0, len(stock_data), 13):  # 一共13列，跳跃间距为13
            content = stock_data[i + 0] + '\t' + stock_data[i + 1] + '\t' + stock_data[i + 2] + '\t' \
                      + stock_data[i + 3] + '\t' + stock_data[i + 4] + '\t' + stock_data[i + 5] + '\t' \
                      + stock_data[i + 6]
            # print(content)
            fos.write(content + '\n')
    print('SUCCESS')
    # 关闭文件
    fos.close()


if __name__ == '__main__':
    filename = time.strftime("%Y-%m-%d_%H%M%S") + '_stock.txt'
    stock_data_write_file(filename)
