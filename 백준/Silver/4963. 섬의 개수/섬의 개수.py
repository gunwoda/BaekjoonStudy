import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def dfs(n,m,point,visited,board):
    di = [1,1,1,0,0,-1,-1,-1]
    dj = [-1,0,1,-1,1,1,0,-1]

    i,j = point
    visited[i][j] = 1

    for p in range(8):
        ni = i+di[p]
        nj = j+dj[p]
        if 0<=ni<n and 0<=nj<m and visited[ni][nj]==0 and board[ni][nj] == 1:
            point = (ni,nj)
            dfs(n,m,point,visited,board)

while True:
    m,n = map(int,input().split())
    if n==0 and m==0:
        break
    board = []
    for _ in range(n):
        board.append(list(map(int,input().split())))
    visited = [[0]*m for _ in range(n)]
    island = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1 and visited[i][j]==0:
                dfs(n,m,(i,j),visited, board)
                island += 1
    print(island)


