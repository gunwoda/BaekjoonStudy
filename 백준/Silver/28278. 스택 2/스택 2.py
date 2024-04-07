import sys
n = int(input())
stack = []
def operation(k):
    if k[0] == 1:
        stack.append(k[1])
    elif k[0]==2:
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
    elif k[0]==3:
        print(len(stack))
    elif k[0]==4:
        if len(stack)==0:
            print(1)
        else :
            print(0)
    elif k[0]==5:
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])

for i in range(n):
    operation(list(map(int,sys.stdin.readline().split())))
