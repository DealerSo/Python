
data = open('data.txt','r',encoding="utf-8")
print(data.readline())
print(data.readline())
data.seek(0)
print(data.readline())
data.close()