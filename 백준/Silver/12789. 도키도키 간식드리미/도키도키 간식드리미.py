
n = int(input())

lst = list(map(int,input().split()))
stack = []
count = 1
for i in range(n):
    stack.append(lst[i])
    while stack and stack[-1]==count:
        stack.pop()
        count = count+1

if len(stack) == 0:
    print('Nice')
else :
    print('Sad')
