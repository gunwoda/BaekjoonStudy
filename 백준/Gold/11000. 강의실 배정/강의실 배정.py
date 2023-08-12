import heapq
import sys
n = int(input())
lst = []
for _ in range(n):
    lst.append(list(map(int,sys.stdin.readline().split())))
lst.sort()
room = []
heapq.heappush(room,lst[0][1])
for i in range(1,n):
    if room[0]>lst[i][0]:
        heapq.heappush(room,lst[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room,lst[i][1])
print(len(room))