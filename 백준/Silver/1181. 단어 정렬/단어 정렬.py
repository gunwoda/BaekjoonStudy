import sys
n = int(input())
lst = set()
for _ in range(n):
    k = sys.stdin.readline().rstrip()
    lst.add(k)
lst = list(lst)
lst.sort()
lst.sort(key= lambda x :len(x))
for i in lst:
    print(i)