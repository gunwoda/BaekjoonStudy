from collections import deque

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

node = [[] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            node[i].append(j)

ans = [[0]*n for _ in range(n)]
visited = []

def dfs(start,current):
    for i in node[current]:
        if visited[i] == 0:
            ans[start][i] = 1
            visited[i] = 1
            dfs(start,i)

for i in range(n):
    visited = [0]*n
    dfs(i,i)

for i in ans:
    print(*i)
