import re

date1 = '11/27/2017'
datepat = re.compile(r'\d+/\d+/\d+')
if datepat.match(date1):
    print('yes')
else:
    print('no')

date = datepat.match(date1)
print(date.group(0))