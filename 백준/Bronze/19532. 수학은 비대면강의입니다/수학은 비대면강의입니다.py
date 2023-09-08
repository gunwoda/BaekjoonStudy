check = False
lst= list(map(int,input().split()))
for x in range(-999,1000):
    for y in range(-999,1000):
        if lst[0]*x+lst[1]*y==lst[2] and lst[3]*x+lst[4]*y==lst[5]:
            print(x,y)
            check = True
            break
    if check:
        break
