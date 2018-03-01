# 导入自定义模块parse
import parse

if __name__ == '__main__':
    animals = ['Dog', 'the name is Lube', 'Cat', 12, ['Tiger', ['the name is Tg', 21, 1.2]],'Pig','lee']
    parse.print_multiple_list(animals,0)    # 调用自定义模块中的方法