#2822

dic = {}
sum = 0
for i in range(8):
    dic[i+1] = int(input())

li = [] #파이썬3에서 dic_items()는 리스트를 반환하지 않음
for k,v in dic.items():
    t = (k,v)
    li.append(t)
li.sort(key=lambda x:x[1],reverse=True)
li = li[0:5]
li.sort(key=lambda x:x[0])
for i in li:
    sum+=i[1]
print(sum)
for i in li:
    print(i[0],end=' ')