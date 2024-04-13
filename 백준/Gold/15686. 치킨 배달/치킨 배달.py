N,M = map(int,input().split())

board = []
for i in range(N):
    board.append(list(map(int,input().split())))

chicken = []
home = []

for i in range(N):
    for k in range(N):
        if board[i][k] == 2:
            chicken.append([i,k])
        elif board[i][k] == 1:
            home.append([i,k])
def combination(arr,n):
    for i in range(len(arr)):
        if n==1:
            yield [arr[i]]
        else:
            for next in combination(arr[i+1:],n-1):
                yield [arr[i]]+next
ans_lst = []
for i in combination(chicken,M):
    total_dis = 0
    for a in home:
        min_dis = 101
        for k in i:
            dis = abs(a[0]-k[0])+abs(a[1]-k[1])
            min_dis = min(min_dis,dis)
        total_dis = total_dis+min_dis
    ans_lst.append(total_dis)
ans_lst.sort()
print(ans_lst[0])