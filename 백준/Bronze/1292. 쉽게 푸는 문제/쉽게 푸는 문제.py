a,b = map(int,input().split())
count = 0
lst = []
for i in range(b):
    count = count+1
    for k in range(count):
        lst.append(count)
lst = lst[a-1:b]
print(sum(lst))
