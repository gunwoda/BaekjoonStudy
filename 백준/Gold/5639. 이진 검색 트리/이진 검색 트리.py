import sys
sys.setrecursionlimit(10 ** 6)

tree = []

while True:
    try:
        tree.append(int(input()))
    except:
        break


def recursive(A):
    if len(A) == 0:
        return
    root = A[0]
    tempL, tempR = [], []
    for i in range(1,len(A)):
        if A[i] > root:
            tempL = A[1:i]
            tempR = A[i:]
            break
    else:
        tempL = A[1:]
    recursive(tempL)
    recursive(tempR)
    print(root)

recursive(tree)