n = int(input())

def find(n):
    cnt = [1,2,4]

    if n>3:
        for i in range(3,n):
            num = cnt[i-1]+cnt[i-2]+cnt[i-3]
            cnt.append(num)
    print(cnt[n-1])

for i in range(n):
    k = int(input())
    find(k)