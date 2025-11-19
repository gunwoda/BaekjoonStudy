import sys
sys.setrecursionlimit(1000000)

n,m = map(int,input().split())
board = []
for _ in range(n):
    board.append(list(map(int,input().split())))



def dfs(point,visited):
    global size
    i,j = point
    visited[i][j] = 1

    di = [0,0,1,-1]
    dj = [1,-1,0,0]

    for p in range(4):
        ni = i+di[p]
        nj = j+dj[p]
        if 0<=ni<n and 0<=nj<m and board[ni][nj] == 1 and visited[ni][nj]==0:
            dfs((ni,nj),visited)
            size+=1

ans_size = 0
cnt = 0
visited = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if board[i][j] == 1 and visited[i][j] == 0:
            size = 1
            dfs((i,j),visited)
            cnt+= 1
            ans_size = max(ans_size,size)
print(cnt)
print(ans_size)
