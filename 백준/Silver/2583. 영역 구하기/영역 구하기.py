import sys
sys.setrecursionlimit(100000)
M,N,K = map(int,input().split())
board = [[0]*N for _ in range(N)]
for _ in range(K):
    x1,y1,x2,y2 = map(int,input().split())
    for i in range(y1,y2):
        for j in range(x1,x2):
            board[i][j] = 1

visited = [[0]*N for _ in range(M)]
def dfs(point,visited):
    global size
    size += 1
    i,j = point
    visited[i][j] = 1
    di = [0,0,1,-1]
    dj = [1,-1,0,0]
    for p in range(4):
        ni = i+di[p]
        nj = j+dj[p]
        if 0<=ni<M and 0<=nj<N and visited[ni][nj] == 0 and board[ni][nj] == 0:
            dfs((ni,nj),visited,)
sizes = []
ans = 0
for i in range(M):
    for j in range(N):
        if board[i][j] == 0 and visited[i][j] == 0:
            size = 0
            dfs((i,j),visited)
            sizes.append(size)
            ans += 1

print(ans)
sizes.sort()
print(*sizes)



