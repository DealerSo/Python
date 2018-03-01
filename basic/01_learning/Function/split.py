import re

# string中的split只能分割一种格式
# re中的split能同时分割多种格式
line = 'abc defh,xyz;ttt ll,aa,bb;cc'
content = re.split('[,; ]', line)
print(content)
