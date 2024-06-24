import sys

input = sys.stdin.readline

n = int(input())

cost = [[0,0,0]]

for _ in range(n):
    cost.append(list(map(int,input().split())))

house = [[0,0,0] for _ in range(n+1)]

for i in range(1,n+1):
    house[i][0] = cost[i][0] + min(house[i-1][1],house[i-1][2])
    house[i][1] = cost[i][1] + min(house[i-1][0],house[i-1][2])
    house[i][2] = cost[i][2] + min(house[i-1][1],house[i-1][0])

print(min(house[n]))