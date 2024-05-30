n = input().split('-')

answer_lst = []

for i in n:
    sum = 0
    lst = i.split('+')
    for k in lst:
        sum = sum+int(k)
    answer_lst.append(sum)

answer = answer_lst[0]


for i in range(1,len(answer_lst)):
    answer = answer - answer_lst[i]

print(answer)