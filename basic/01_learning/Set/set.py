# set和dict类似，也是一组key的集合，但不存储value
# 定义方式：set([])

numbers = set([1,2,3])
numbers.add(4)
numbers.add(5)
numbers.add(4)
print(numbers)