word = list(input())
bomb = input()
n = len(bomb)
left = 0
flag = True
stack = []
for i in word:
    stack.append(i)
    if ''.join(stack[-n:]) == bomb:
        for _ in range(n):
            stack.pop()
if stack:
    print(''.join(stack))
else:
    print('FRULA')




