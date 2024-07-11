import sys
from collections import deque
r,c = map(int,input().split())

graph = []
visited = set()
for i in range(r):
    graph.append(list(input()))
dy = [0,0,1,-1]
dx = [1,-1,0,0]
max_count = 0
def dfs(y,x,count):
    global max_count
    max_count = max(max_count,count)
    for i in range(4):
        n_y,n_x = y+dy[i],x+dx[i]
        if 0<=n_y<r and 0<=n_x<c:
            if graph[n_y][n_x] not in visited:
                visited.add(graph[n_y][n_x])
                dfs(n_y,n_x,count+1)
                visited.remove(graph[n_y][n_x])
visited.add(graph[0][0])
dfs(0,0,1)
print(max_count)