import heapq
import sys

input = sys.stdin.readline

n = int(input())
bus = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(bus):
    start,end,cost = map(int,input().split())
    graph[start].append((end,cost))

def dijkstra(s):
    INF = float('inf')
    dp = [INF]*(n+1)
    dp[s] = 0
    heap = []
    heapq.heappush(heap, (0,s))
    while heap:
        dist,now = heapq.heappop(heap)
        if dp[now] < dist:
            continue
        for next,c in graph[now]:
            cost = dist+c
            if dp[next] > cost:
                dp[next] = cost
                heapq.heappush(heap,(cost,next))
    for i in range(n+1):
        if dp[i] == INF:
            dp[i] = 0
    return dp[1:]

for i in range(1,n+1):
    ans = dijkstra(i)
    print(*ans)