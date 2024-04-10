from collections import deque

n,m,v = map(int,input().split())
lst = [[] for _ in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    lst[a].append(b)
    lst[b].append(a)

for i in lst:
    i.sort()


visited = [0]*(n+1)
answer = []
def dfs(start_node):
    answer.append(start_node)
    visited[start_node] = 1
    for i in lst[start_node]:
        if not visited[i]:
            dfs(i)

dfs(v)
print(*answer)

visited = [0]*(n+1)
answer = []

def bfs(start_node):
    deq = deque()
    deq.append(start_node)
    while deq:
        node = deq.popleft()
        visited[node] = 1
        answer.append(node)        
        for i in lst[node]:
            if not visited[i] and i not in deq:
                deq.append(i)

bfs(v)
print(*answer)
