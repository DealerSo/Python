class Programmer(object):
    hobby = 'Play Computer'

    # 构造函数

    def __init__(self, name, age, weight):
        # 公用的属性
        self.name = name
        # 使用的属性，但是没有被限制，只是区分一下
        self._age = age
        self.__weight = weight

    # @classmethod 表示是类方法，直接可以用Programmer.get_hobby()进行调用
    @classmethod
    def get_hobby(cls):
        return cls.hobby

    # @property 属性方法，用实例化类的对象进行调用，但不需要加括号，和调动属性一样
    # 如：类的对象名为programer，programer.get_weight调用即可，不用加括号。
    @property
    def get_weight(self):
        return self.__weight

    # 正常类方法名，使用类的对象名调用即可，programer.introduction()
    def self_introduction(self):
        print('My Name is %s \n I am %s years old' % (self.name, self._age))


# 继承Programmer类
class SubProgrammer(Programmer):
    def __init__(self, name, age, weight, language):
        # 调用父类的构造函数
        super(SubProgrammer, self).__init__(name, age, weight)
        self.language = language

    # 重写父类方法
    def self_introduction(self):
        print('My Name is %s \n My favorite language is %s ' % (self.name, self.language))


# 实现多态，不同对象出现不同形态
def introduction(programer):
    if isinstance(programer, Programmer):
        programer.self_introduction()

if __name__ == '__main__':
    subProgramer = SubProgrammer('Vincent', 31, 85, 'Python')
    print(dir(subProgramer))
    print(subProgramer.__dict__)
    print(Programmer.get_hobby())
    print(subProgramer.get_weight)
    # programer.self_introduction()
    # print(isinstance(programer, Programmer))
    introduction(subProgramer)
    print()
    programer = Programmer('Lisa', 28, 48)
    introduction(programer)