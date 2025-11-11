test_case = int(input())
for _ in range(test_case):
    start,end = map(int,input().split())
    numerator = 1
    denominator = 1
    for i in range(start):
        numerator = numerator*(end-i)
    for j in range(1,start+1):
        denominator *= j

    ans = numerator/denominator
    print(int(ans))




