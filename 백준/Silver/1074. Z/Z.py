
n,r,c = map(int,input().split())
count = 0
while n!=0:
    n = n-1
    if 2**(n)>r and 2**n>c:
        pass
    elif 2**n>r and 2**n<=c:
        count = count + 2**(2*n)*1
        c = c-2**n
    elif 2**n<=r and 2**n>c:
        count = count + 2**(2*n)*2
        r = r-2**n
    elif 2**n<=r and 2**n<=c:
        count = count + 2**(2*n)*3
        r = r-2**n
        c = c-2**n
print(count)