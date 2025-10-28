import heapq
import sys
input = sys.stdin.readline
n = int(input())
heap = []
for _ in range(n):
    oper = int(input())
    if oper != 0:
        heapq.heappush(heap,(abs(oper),oper))
    else:
        if len(heap) == 0:
            print(0)
        else:
            _,output = heapq.heappop(heap)
            print(output)
