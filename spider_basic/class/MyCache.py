import datetime
import random

class MyCache:
    # --------------------------------------------------------
    def __init__(self):
        self.cache = {}
        self.max_cache_size = 10

    # --------------------------------------------------------
    def __contains__(self, key):
        '''
        根据该项是否存在于缓存当中返回True或者False
        :param item:
        :return:
        '''
        return key in self.cache

    def update(self, key, value):
        '''
        更新该缓存字典，可以选择性删除最早条目
        :param item:
        :param value:
        :return:
        '''
        if key not in self.cache and len(self.cache) >= self.max_cache_size:
            pass
        self.cache[key] = {'date_accessed': datetime.datetime.now(), 'value': value}

    def remove(self):
        '''
        删除具备最早访问日期的输入数据
        :return:
        '''
        oldest_key = None
        for key in self.cache:
            if oldest_key == None:
                oldest_key = key
            elif self.cache[key]['date_accessed'] < self.cache[oldest_key]['date_accessed']:
                oldest_key = key
        self.cache.pop(oldest_key)

    # @property 提供get方法，能使用getSize()进行调用
    @property
    def size(self):
        '''
        返回缓存容量大小
        :return:
        '''
        return len(self.cache)

    # @size.setter提供set方法
    @size.setter
    def size(self, value):
        pass


if __name__ == '__main__':
    pass