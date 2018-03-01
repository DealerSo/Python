# 元组
# 定义方式： t()

# 元组的特点，一旦被定义指向就不能被修改
languages = ('Java', 'Python', 'Vue')
print(languages[1])


# 但是有一种情况元组是可以“修改”的，其实修改元组值对应的应用，看下下面的例子
classmates = ('Michael', 'Jacky', 'Tom', ['lili', 'Marry'])
classmates[3][0] = 'Vincent'
classmates[3][1] = 'Jojo'
print(classmates)

# 上述例子：表面上看tuple(元组)中的元素确实变了，但其实变的不是tuple的元素，而是
# tuple中list的元素，tuple一开始志祥的list并没有改成别的list，所以tuple所谓的
# “不变”是说，tuple的每个元素，指向永远不变(tuple中每个对象内存中的指向)。可以看tuple.png
