from collections import deque

n = int(input())

def bfs(n):
    q = deque()
    q.append([n])
    count = 0
    while q:
        lst = []
        i = q.pop()
        if 1 in i:
            return count
        for k in i:
            if k%3 == 0:
                lst.append(k//3)
            if k%2 == 0:
                lst.append(k//2)
            lst.append(k-1)
        q.append(lst)
        count = count+1

print(bfs(n))