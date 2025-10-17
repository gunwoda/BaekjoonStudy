import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int,input().split())
board = []
for _ in range(n):
    board.append(list(map(int,input().split())))
flag = True
si,sj = 0,0
for i in range(n):
    for j in range(m):
        if board[i][j]==2:
            si,sj = i,j
            flag = False
            break
    if not flag:
        break
ans = [[-1]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            ans[i][j] = 0

dx = [1,-1,0,0]
dy = [0,0,1,-1]

q = deque()
q.append((si,sj))
ans[si][sj] = 0
while q:
    i,j = q.popleft()
    for p in range(4):
        ni = i+dy[p]
        nj = j+dx[p]
        if 0<=ni<n and 0<=nj<m and ans[ni][nj] == -1:
            ans[ni][nj] = ans[i][j]+1
            q.append((ni,nj))
for i in ans:
    print(*i)
