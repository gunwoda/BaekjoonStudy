import sys
from collections import defaultdict
input = sys.stdin.readline
n = int(input())
num = list(map(int,input().split()))
arr = sorted(set(num))
dic = {arr[i] : i for i in range(len(arr))}
ans = []
for i in num:
    ans.append(dic[i])
print(*ans)