n = int(input())
ex = len(str(n))
cnt = int(input())
if cnt == 0 :
    cnt_lst = []
else :
    cnt_lst = list(map(int,input().split(' ')))
current_channel = 100
btn_cnt = abs(n-current_channel)
channel_lst = []
channel = 0
check = True
click = 0
if 10**(ex+1) > 1000000:
    max = 1000000
else :
    max = 10**(ex+1)

for i in range(int(10**(ex-2)-1),int(max)):
    for k in cnt_lst:
        if str(k) in str(i):
            check = False
    if check:
        if abs(btn_cnt)>(abs(n-i)+len(str(i))):
            btn_cnt = abs(n-i)+len(str(i))
    check = True
print(btn_cnt)


