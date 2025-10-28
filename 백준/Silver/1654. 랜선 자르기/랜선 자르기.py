import sys
input = sys.stdin.readline

n, m = map(int, input().split())
line = [int(input()) for _ in range(n)]

# 상한: 문제 성격에 따라 선택
# - '최대 길이'를 찾는 랜선 자르기면 right = max(line)
# - 'm명에게 같은 수량을 나눌 때 1인당 최대 수량'이면 right = sum(line) // m
right = max(line)
left = 1
ans = 0

while left <= right:
    mid = (left + right) // 2  # 시도하는 1인당 수량(정수)
    cnt = 0
    for x in line:
        cnt += x // mid

    if cnt >= m:
        # mid 만큼씩 주는 게 가능 → 더 키워본다
        ans = mid
        left = mid + 1
    else:
        # mid 만큼씩은 불가능 → 줄인다
        right = mid - 1

print(ans)
