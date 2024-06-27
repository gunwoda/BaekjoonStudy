# 1753

import heapq
import sys

input = sys.stdin.readline

INF = float('inf')

v,e = map(int,input().split())

start = int(input())

graph = [[] for _ in range(v+1)]

for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))



def dijkstra(start):
    table = [INF]*(v+1)
    table[start] = 0
    q = []
    heapq.heappush(q,(0,start))
    while q:
        dist, node = heapq.heappop(q)
        for i in graph[node]:
            idx = i[0]
            cost = dist+i[1]
            if cost < table[idx]:
                table[idx] = cost
                heapq.heappush(q,(cost,idx))
    return table
    
table = dijkstra(start)
for i in range(1,v+1):
    if table[i] == INF:
        print('INF')
    else:
        print(table[i])
