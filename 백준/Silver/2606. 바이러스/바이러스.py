from collections import deque

node = int(input())
vertex = int(input())
lst = [[] for _ in range(node+1)]
for i in range(vertex):
    a,b = map(int,input().split())
    lst[a].append(b)
    lst[b].append(a)
def bfs(start_node):
    deq = deque()
    visited = [0]*(node+1)
        
    deq.append(start_node)
    while deq:
        n = deq.popleft()
        for i in lst[n]:
            if visited[i] == 0 and i not in deq:
                visited[i] = 1
                deq.append(i)
    ans = sum(visited)
    if ans == 0:
        return 0
    else :
        return ans-1

print(bfs(1))
