from fnmatch import fnmatch, fnmatchcase

# 匹配文件,可以使用正则表达式
# print(fnmatch('foo.txt','*.txt'))

# filenames = ['Date1.csv', 'Date2.csv', 'config.ini', 'foo.py']
# for filename in filenames:
#     if fnmatch(filename, 'Date[0-9]*'):
#         print(filename + "....")
#     else:
#         print(filename)

addresses = ['5412 N CLARK ST', '1060 W ADDISON ST', '2122 N CLARK ST']
for address in addresses:
    if fnmatchcase(address, '54[0-9][0-9] *CLARK*'):
        print(address + "...")
    else:
        print(address)
