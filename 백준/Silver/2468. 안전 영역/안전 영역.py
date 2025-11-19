import sys
sys.setrecursionlimit(1000000)


n = int(input())

board = []

for _ in range(n):
    board.append(list(map(int,input().split())))


def dfs(point,visited,deepth):
    i,j = point
    di = [0,0,1,-1]
    dj = [1,-1,0,0]
    for p in range(4):
        ni = di[p]+i
        nj = dj[p]+j
        if 0<=ni<n and 0<=nj<n and visited[ni][nj] == 0 and board[ni][nj] > deepth:
            visited[ni][nj] = 1
            point = (ni,nj)
            dfs(point,visited, deepth)

top_floor = 0

for i in range(n):
    top_floor = max(top_floor,max(board[i]))

ans = 0
for depth in range(top_floor):
    visited = [[0]*n for _ in range(n)]
    room = 0
    for i in range(n):
        for j in range(n):
            point = (i,j)
            if board[i][j] > depth and visited[i][j] == 0:
                room += 1
                dfs(point, visited, depth)
    ans = max(room,ans)

print(ans)