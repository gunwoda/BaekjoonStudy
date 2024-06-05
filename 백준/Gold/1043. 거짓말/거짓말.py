import sys

input = sys.stdin.readline

N,M = map(int,input().split())
knowlist = set(input().split()[1:])
party = []
for _ in range(M):
    party.append(set(input().split()[1:]))

for _ in range(M):
    for parties in party:
        if parties & knowlist:
            knowlist = knowlist.union(parties)
cnt = 0
for parties in party:
    if parties & knowlist:
        continue
    cnt = cnt+1
print(cnt)
