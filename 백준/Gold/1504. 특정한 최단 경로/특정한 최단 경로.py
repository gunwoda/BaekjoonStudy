# 1504
import sys
import heapq

input = sys.stdin.readline
node, vertex = map(int,input().split())
graph = [[]for _ in range(node+1)]
for i in range(vertex):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

vertex1,vertex2 = map(int,input().split())

INF = float('inf')

def dijkstra(start):
    table = [INF]*(node+1)
    table[start] = 0
    q = []
    heapq.heappush(q,(0,start))
    while q:
        d, n = heapq.heappop(q)
        for i in graph[n]:
            cost = d+i[1]
            if table[i[0]]>cost:
                table[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
    return table

cost1 = dijkstra(1)[vertex1]
cost2 = dijkstra(vertex1)[vertex2]
cost3 = dijkstra(vertex2)[node]
cost_1 = cost1+cost2+cost3
cost4 = dijkstra(1)[vertex2]
cost5 = dijkstra(vertex2)[vertex1]
cost6 = dijkstra(vertex1)[node]
cost_2 = cost4+cost5+cost6
answer = min(cost_1,cost_2)
if answer == INF:
    print(-1)
else:
    print(answer)
