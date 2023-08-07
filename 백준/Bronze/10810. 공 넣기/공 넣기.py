a,b = map(int,input().split(' '))
lst = []
for i in range(b):
    lst.append(list(map(int,input().split(' '))))

basket = [0]*a

for i in lst:
    for k in range(i[0]-1,i[1]):
        basket[k]=i[2]
for i in basket:
    print(i,end=' ')
