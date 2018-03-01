# -*- coding: utf-8 -*-
from urllib import request
import http.client


def print_lines(lines):
    for line in lines:
        for l in line:
            print(l, end=',')
        print()


def method(list):
    for m in list:
        print(m)


def read_content():
    resp = request.urlopen("http://www.sina.com.cn")  # type: http.client.HTTPResponse
    # lines = resp.readlines()
    # print_lines(lines)
    # msg = resp.info()  # type: http.client.HTTPMessage
    # print_lines(msg.items())
    print(resp.headers)
    print(resp.getheader("Content-Type"))
    method(dir(resp))


def retrieve():
    filename, content = request.urlretrieve("http://www.sina.com.cn", "index.html")
    print(filename)
    print(content)

# main 函数,和Java main方法是一样的性质
if __name__ == '__main__':
    retrieve()
