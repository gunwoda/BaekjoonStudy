import sys
import heapq
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]

for i in range(n-1):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

INF = 1e9
def dijkstra(start):
    table = [INF]*(n+1)
    table[0] = 0
    table[start] = 0
    q = []
    heapq.heappush(q,(0,start))
    while q:
        dist,cur = heapq.heappop(q)
        for i in graph[cur]:
            cost = dist+i[1]
            if cost<table[i[0]]:
                table[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
    return table
idx_table = []
idx = 0
if n == 1:
    print(0)
else:        
    table = dijkstra(1)
    min_value = max(table[2:])
    ans_lst = []
    for i in range(len(table)):
        if table[i] == min_value:
            ans_lst.append(i)
    max_value = 0
    for i in ans_lst:
        max_v = max(dijkstra(i))
        max_value = max(max_value,max_v)
    print(max_value)