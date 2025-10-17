import sys
input = sys.stdin.readline
from collections import defaultdict,deque
n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0]*(n+1)

def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = 1
    while q:
        cur = q.popleft()
        for i in graph[cur]:
            if visited[i] == 0:
                visited[i] = 1
                q.append(i)

cnt = 0
for i in range(1,n+1):
    if visited[i] == 0:
        bfs(i)
        cnt+=1
print(cnt)
