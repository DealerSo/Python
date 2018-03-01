# 列表
# 定义方式：l = []

classmates = ['Michael', 'Jacky', 'Tom']
# 数组长度
print(len(classmates))

for classmate in classmates:
    index = len(classmates) - 1
    if classmate == classmates[index]:
        print(classmate, end='')
    else:
        print(classmate, end=',')
print()
# 数组尾部添加元素,append()
classmates.append('Marry')
for classmate in classmates:
    print(classmate, end=',')

print()
# 数组任意位置添加元素,insert()
classmates.insert(1, 'lili')
for classmate in classmates:
    print(classmate, end=',')

print()
# 删除数组最后元素,pop()
# 删除具体数组哪个元素,pop(1)，删除数组下标为1的元素
classmates.pop()
for classmate in classmates:
    print(classmate, end=',')

print()
languages = ['Java', 'Python', ['H5', 'Vue'], 'C++']
for language in languages:
    # 判断language是否为list类型，如果是返回true
    if isinstance(language, list):
        for lang in language:
            print(lang, end=',')
    else:
        print(language, end=',')
