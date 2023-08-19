import sys
from collections import deque
n = int(input())

lst = []
for i in range(n):
    lst.append(list(map(int,sys.stdin.readline().split())))

shark = []
fish = []
for i in range(len(lst)):
    for k in range(len(lst[0])):
        if lst[i][k] == 9:
            shark.append(i)
            shark.append(k)
            lst[i][k] = 0
queue = deque()
queue.append([shark[0],shark[1]])

dx = [0,-1,1,0]
dy = [-1,0,0,1]

def bfs(lst,size):
    visitied = [[0]*n for _ in range(n)]
    ans_lst = []
    while queue:
        p,q = queue.popleft()
        for i in range(4):
            if 0<=dy[i]+p<n and 0<=dx[i]+q<n :
                if not visitied[dy[i]+p][dx[i]+q]:                    
                    if lst[dy[i]+p][dx[i]+q] ==0 or lst[dy[i]+p][dx[i]+q] == size:
                        visitied[dy[i]+p][dx[i]+q] = visitied[p][q]+1
                        queue.append([dy[i]+p,dx[i]+q])
                    elif lst[dy[i]+p][dx[i]+q]<size:
                        visitied[dy[i]+p][dx[i]+q] = visitied[p][q]+1
                        ans_lst.append([visitied[dy[i]+p][dx[i]+q],dy[i]+p,dx[i]+q])
    
    if len(ans_lst)>0:
        ans_lst.sort(key=lambda x:x[2])
        ans_lst.sort(key=lambda x:x[1])
        ans_lst.sort(key=lambda x:x[0])
        lst[ans_lst[0][1]][ans_lst[0][2]] = 0
        return ans_lst[0][0],ans_lst[0][1],ans_lst[0][2]
    else :
        return 0,0,0
sum = 0
size = 2
cnt = 0
while True:
    a,b,c = bfs(lst,size)
    if a==0 and b==0 and c==0:
        break
    sum = sum+a
    queue.clear()
    queue.append([b,c])
    cnt = cnt+1
    if cnt==size:
        cnt = 0
        size = size+1
print(sum)
