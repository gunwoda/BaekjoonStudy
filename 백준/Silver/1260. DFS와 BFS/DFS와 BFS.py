from collections import deque

a,b,c = map(int,input().split())
lst = [[] for _ in range(a)]
for _ in range(b):
    p,q = map(int,input().split())
    lst[p-1].append(q-1)
    lst[q-1].append(p-1)
for i in lst:
    i.sort()
def dfs_process(start_node):
    visited = [0 for _ in range(a)]
    ret_lst = []

    def dfs(start_node):
        visited[start_node] = 1
        ret_lst.append(start_node)
        for i in lst[start_node]:
            if i not in ret_lst:
                dfs(i)
    dfs(start_node)
    result_lst = []
    for i in ret_lst:
        result_lst.append(i+1)
    print(*result_lst)

def bfs_process(start_node):
    visited = [0 for _ in range(a)]
    queue = deque([start_node])
    ret_lst = []
    while queue:
        k = queue.popleft()
        if k+1 not in ret_lst: 
            ret_lst.append(k+1)
        visited[k] = 1
        for i in lst[k]:
            if visited[i] == 0:
                queue.append(i)
    print(*ret_lst)
dfs_process(c-1)
bfs_process(c-1)