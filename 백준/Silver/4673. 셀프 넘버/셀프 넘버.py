lst = set()
for i in range(1,10001):
    lst.add(i)
for i in range(1,10001):
    sum = i
    for k in str(i):
        sum = sum+int(k)
    lst.discard(sum)

for i in lst:
    print(i)
        
    