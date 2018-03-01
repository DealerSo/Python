# 从python发布工具distutils.core中导入setup方法
from distutils.core import setup

setup(
    name                = 'parse',                   # 之后使用这个模块时import的名字
    version             = '1.0.0',                   # 版本
    py_modules          = ['parse'],                 # 模块名
    author              = 'abc',
    author_email        = 'abc@163.com',
    url                 = 'http://www.abc.com',
    description         = 'A simple printer of animals lists'
)