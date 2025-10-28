import sys

from collections import deque

input = sys.stdin.readline

n,m = map(int,input().split())
board = []
for _ in range(n):
    board.append(list(input().strip()))
flag = False
si,sj = 0,0
for i in range(n):
    for j in range(m):
        if board[i][j] == 'I':
            si,sj = i,j
            flag = True
            break
    if flag:
        break


q =deque()
q.append((si,sj))
visited = [[0]*m for _ in range(n)]
visited[si][sj] = 1
dx = [0,0,1,-1]
dy = [1,-1,0,0]
cnt = 0
while q:
    i,j = q.popleft()
    for p in range(4):
        ni = i+dy[p]
        nj = j+dx[p]
        if 0<=ni<n and 0<=nj<m and board[ni][nj] != 'X' and visited[ni][nj] == 0:
            if board[ni][nj] == 'P':
                cnt += 1
            visited[ni][nj] = 1
            q.append((ni,nj))
if cnt == 0:
    print('TT')
else:
    print(cnt)

