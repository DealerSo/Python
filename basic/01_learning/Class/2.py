class Programer(object):
    def __init__(self, name, age):
        self.name = name
        if isinstance(age, int):
            self.age = age
        else:
            raise Exception('age must be int')

    # 重写魔术方法 __eq__ 和 __add__方法
    def __eq__(self, other):
        if isinstance(other, Programer):
            if self.age == other.age:
                return True
            else:
                return False
        else:
            raise Exception('The type of object must be Programer')

    def __add__(self, other):
        if isinstance(other, Programer):
            return self.age + other.age
        else:
            raise Exception('The type of object must be Programer')


if __name__ == '__main__':
    p1 = Programer('Vincent', 22)
    p2 = Programer('Jacky', 25)

    print(p1 == p2)
    print(p1 + p2)
