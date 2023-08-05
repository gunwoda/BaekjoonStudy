n,m,y,x,k = map(int,input().split())
lst = []
for i in range(n):
    lst.append(list(map(int,input().split())))
cmd_lst = list(map(int,input().split()))
dice = [0,0,0,0,0,0]

def west():
    temp = dice[0]
    dice[0] = dice[2]
    dice[2] = dice[5]
    dice[5] = dice[3]
    dice[3] = temp

def east():
    temp = dice[0]
    dice[0] = dice[3]
    dice[3] = dice[5]
    dice[5] = dice[2]
    dice[2] = temp

def north():
    temp = dice[0]
    dice[0] = dice[4]
    dice[4] = dice[5]
    dice[5] = dice[1]
    dice[1] = temp

def south():
    temp = dice[0]
    dice[0] = dice[1]
    dice[1] = dice[5]
    dice[5] = dice[4]
    dice[4] = temp


for i in cmd_lst:
    if i == 1 and x<m-1:
        east()
        x = x + 1
        if lst[y][x] == 0:
            lst[y][x] = dice[5]
            print(dice[0])
        else:
            dice[5] = lst[y][x]
            lst[y][x] = 0
            print(dice[0])
    elif i == 2 and x>0:
        west()
        x = x - 1
        if lst[y][x] == 0:
            lst[y][x] = dice[5]
            print(dice[0])
        else:
            dice[5] = lst[y][x]
            lst[y][x] = 0
            print(dice[0])
    elif i == 3 and y>0:
        north()
        y = y - 1
        if lst[y][x] == 0:
            lst[y][x] = dice[5]
            print(dice[0])
        else:
            dice[5] = lst[y][x]
            lst[y][x] = 0
            print(dice[0])
    elif i == 4 and y<n-1:
        south()
        y = y + 1
        if lst[y][x] == 0:
            lst[y][x] = dice[5]
            print(dice[0])
        else:
            dice[5] = lst[y][x]
            lst[y][x] = 0
            print(dice[0])

