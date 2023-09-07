n = int(input())
check = True
for i in range(n):
    num = i
    for k in str(i):
        num = num+int(k)
    if num == n:
        check = False
        print(i)
        break
if check:
    print(0)
