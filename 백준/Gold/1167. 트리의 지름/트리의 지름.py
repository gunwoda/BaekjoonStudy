import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

tree_value = dict()
graph = [[]for _ in range(n+1)]

for _ in range(1,n+1):
    info = list(map(int,input().split()))
    p = 1
    lst = []
    while True:
        start_node = info[0]
        node = info[p]
        if node == -1:
            break
        graph[start_node].append(node)
        value = info[p+1]
        tree_value[(start_node,node)] = value
        p = p+2

answer_list = []

def bfs(start):
    q = deque()
    q.append(start)
    visited = [False for _ in range(n+1)]
    cost = [0 for _ in range(n+1)]
    while q:
        p = q.popleft()
        visited[p] = True
        for i in graph[p]:
            if not visited[i]:
                cost[i] = cost[p]+tree_value[(p,i)]
                q.append(i)
    return cost

cost = bfs(1)

node = 0
for i in range(1,n+1):
    if cost[node]<cost[i]:
        node = i
print(max(bfs(node)))





