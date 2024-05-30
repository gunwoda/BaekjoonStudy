import sys

name, problem = map(int,input().split())
name_lst = {}
name_lst_2 = {}
for i in range(1,name+1):
    k = sys.stdin.readline().strip()
    name_lst[i] = k
    name_lst_2[k] = i
for i in range(problem):
    prob = sys.stdin.readline().strip()
    try:
        pro = int(prob)
        print(name_lst.get(pro))
    except:
        print(name_lst_2.get(prob))
