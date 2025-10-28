import sys

input = sys.stdin.readline

n = int(input())
S = ''
for i in range(2*n+1):
    if i%2 == 0:
        S+='I'
    else:
        S+='O'
m = int(input())
arr = input().strip()
cnt = 0
for i in range(m-(2*n+1)+1):
    if arr[i:i+2*n+1] == S:
        cnt+=1

print(cnt)