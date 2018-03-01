# 累加
def mySum(grades):
    val = 0
    for grade in grades:
        val = val + grade
    return val

# 求平均值
def myAvg(grades):
    return mySum(grades) / len(grades)

# 去除最小值和最大值，然后求平均值
def drop_first_last(grades):
    # *号表示多个参数
    # sorted排序
    first, *middle, last = sorted(grades)
    print(middle)
    print(myAvg(middle))


grades = [1, 5, 6, 7, 2, 9, 8, 3]

drop_first_last(grades)
