from collections import deque, defaultdict
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
up = defaultdict(int)
down = defaultdict(int)

for _ in range(n):
    s, e = map(int, input().split())
    up[s] = e

for _ in range(m):
    s, e = map(int, input().split())
    down[s] = e

# 거리 배열 (칸 1~100), -1은 아직 도달 못함
dist = [-1] * 101
dist[1] = 0

q = deque([1])

while q:
    cur = q.popleft()
    if cur == 100:
        print(dist[cur])
        break

    for dice in range(1, 7):
        next_num = cur + dice
        if next_num > 100:
            continue

        # 사다리/뱀 적용
        if next_num in up:
            next_num = up[next_num]
        elif next_num in down:
            next_num = down[next_num]

        # 처음 방문일 때만 큐에 넣기
        if dist[next_num] == -1:
            dist[next_num] = dist[cur] + 1
            q.append(next_num)
