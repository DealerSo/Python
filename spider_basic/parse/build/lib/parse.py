def print_multiple_list(items,level=0):
    for item in items:
        # 判断item是否为list类型
        if isinstance(item, list):
            print_multiple_list(item,level+1)
        else:
            for i in range(level):
                print('\t',end='')
            print(item)


