import os
import re

def fatch_data_from_file(file_name):
    # 判断文件是否存在
    if os.path.exists(file_name):
        fos = open(file_name,'r',encoding="utf-8")
        # 读取所有行
        lines = fos.read()
        # 查询所有<loc></loc>
        locations = re.findall('<loc>(.*?)</loc>',lines)
        # 循环读取每一行
        for line in locations:
            print(line)
        fos.close()
    else:
        open(file_name, 'a')   # 'a'追加,如果文件不存在会创建一个文件

if __name__ == '__main__':
    fatch_data_from_file("data.txt")