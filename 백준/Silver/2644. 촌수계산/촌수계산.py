n = int(input())
start,end = map(int,input().split())
k = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(k):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

ans = []
def dfs(cur,cnt,end,visited):
    if cur == end:
        ans.append(cnt)
    visited[cur] = 1
    for i in graph[cur]:
        if visited[i] == 0:
            dfs(i,cnt+1,end,visited)

dfs(start,0,end,[0]*(n+1))
if len(ans) == 0:
    print(-1)
else:
    print(ans[0])


