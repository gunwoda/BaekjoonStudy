n = int(input())
lst = list(map(int,input().split()))
count = 1
stack = []

for i in lst:
    stack.append(i)
    while stack and stack[-1] == count:
        stack.pop()
        count = count+1

if stack:
    print('Sad')
else:
    print('Nice')