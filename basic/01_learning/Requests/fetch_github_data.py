import requests
import json

# 通过github api获取github中的数据

# github api地址
URL = 'https://api.github.com'

'''
    Python中的join()函数用法
    join()：    连接字符串数组。将字符串、元组、列表中的元素以指定的字符(分隔符)连接生成一个新的字符串
    
    语法：  'sep'.join(seq)
    参数说明
    sep：分隔符。可以为空
    seq：要连接的元素序列、字符串、元组、字典      
'''
def build_url(endpoint):
    return '/'.join([URL, endpoint])


'''
    json.dumps()  -- 将Python对象编码成JSON字符串，indent=4 四个缩进
    json.loads()  -- 将已编码的JSON字符串解码为Python对象
'''
def better_print(json_data):
    return json.dumps(json.loads(json_data), indent=4)


def fetch_user_info():
    response = requests.get(build_url('users/DealerSo'))
    print(better_print(response.text))


'''
    auth=('username','password') 增加身份认证
    许多要求身份认证的web服务都接受HTTP Basic Auth。这是最简单的一种身份认证，并且Requests对这种认证方式的支持是直接开箱即可用
'''
def fetch_user_email():
    response = requests.get(build_url('user/emails'), auth=('DealerSo', 'abcd1234@@'))
    print(better_print(response.text))


def fetch_users_info():
    response = requests.get(build_url('users'), params={'since': 31})
    print(better_print(response.text))
    print(response.url)


if __name__ == '__main__':
    # fetch_user_info()
    # fetch_user_email()
    fetch_users_info()