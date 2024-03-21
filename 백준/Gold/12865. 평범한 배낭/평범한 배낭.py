from itertools import permutations
n,k = map(int,input().split())
total_list = [[0,0]]
for i in range(n):
    total_list.append(list(map(int,input().split(' '))))
chart = [[0]*(k+1)for _ in range(n+1)]

for n in range(1,n+1):
    for m in range(1,k+1):
        w = total_list[n][0]
        v = total_list[n][1]
        if m<w:
            chart[n][m] = chart[n-1][m]
        else:
            chart[n][m] = max(chart[n-1][m],v+chart[n-1][m-w])
print(chart[n][k])
