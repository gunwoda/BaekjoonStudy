def recursive(str,i,l,count):
    count=count+1
    if (l<=i):
        return 1,count
    elif (str[l]!=str[i]):
        return 0,count
    else :
        return recursive(str,i+1,l-1,count)

def isPalindrome(str,count=0):
    return recursive(str,0,len(str)-1,count)

n = int(input())
for i in range(n):
    k = input()
    count = 0
    a,b = isPalindrome(k,count)
    print(a,b)