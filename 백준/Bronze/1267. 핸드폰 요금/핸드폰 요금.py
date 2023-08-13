n = int(input())
lst = (list(map(int,input().split())))
sum1 = 0
sum2 = 0
for i in lst:
    sum1 = sum1+10*(i//30+1)
    sum2 = sum2+15*(i//60+1)
if sum1<sum2:
    print('Y',sum1)
elif sum2<sum1:
    print('M',sum2)
else:
    print('Y','M',sum1)
    