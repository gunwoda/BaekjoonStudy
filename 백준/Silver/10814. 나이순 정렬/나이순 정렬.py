n = int(input())
lst = []
for _ in range(n):
    lst.append(input().split())
for i in lst:
    i[0] = int(i[0])

lst.sort(key=lambda x:x[0])
for i in lst:
    print(*i)
