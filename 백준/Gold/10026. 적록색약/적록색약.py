from collections import deque

n = int(input())
board = []
visited_normal = [[0]*n for _ in range(n)]
visited_RG = [[0]*n for _ in range(n)]

for _ in range(n):
    board.append(list(input()))

normal_cnt = 0
RG_cnt = 0
di = [0,0,1,-1]
dj = [1,-1,0,0]

def bfs_normal(i,j,color):
    visited_normal[i][j] = 1
    q = deque()
    q.append((i,j))
    while q:
        curi,curj = q.popleft()
        for next in range(4):
            ni = curi+di[next]
            nj = curj+dj[next]
            if 0<=ni<n and 0<=nj<n and visited_normal[ni][nj] == 0:
                if board[ni][nj] == color:
                    visited_normal[ni][nj] = 1
                    q.append((ni,nj))

def bfs_RG(i,j,color):
    visited_RG[i][j] = 1
    q = deque()
    q.append((i,j))
    while q:
        curi,curj = q.popleft()
        for next in range(4):
            ni = curi+di[next]
            nj = curj+dj[next]
            if 0<=ni<n and 0<=nj<n and visited_RG[ni][nj] == 0:
                if color == 'R' or color == 'G':
                    if board[ni][nj] == 'R' or board[ni][nj] == 'G':
                        visited_RG[ni][nj] = 1
                        q.append((ni,nj))
                else:
                    if board[ni][nj] == color:
                        visited_RG[ni][nj] = 1
                        q.append((ni,nj))



for i in range(n):
    for j in range(n):
        if visited_normal[i][j] == 0:
            bfs_normal(i,j,board[i][j])
            normal_cnt+= 1
        if visited_RG[i][j] == 0:
            bfs_RG(i,j,board[i][j])
            RG_cnt+= 1

di = [0,0,1,-1]
dj = [1,-1,0,0]

print(normal_cnt,RG_cnt)




