
n = input()
check = False
for i in range(1, len(n)):
    mul_a = 1
    mul_b = 1
    a = n[:i]
    b = n[i:]
    for i in a:
        mul_a = mul_a*int(i)
    for i in b:
        mul_b = mul_b*int(i)
    if mul_a == mul_b:
        check = True
        break

if check:
    print('YES')
else:
    print('NO')