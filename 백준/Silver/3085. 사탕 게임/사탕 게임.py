def test(lst):
    cnt_lst = []
    for i in range(len(lst)):
        cnt_row = 1
        for k in range(len(lst)-1):
            if lst[i][k] != lst[i][k+1]:
                cnt_row = 0
            cnt_row += 1
            cnt_lst.append(cnt_row)
    
    for i in range(len(lst)):
        cnt_column = 1
        for k in range(len(lst)-1):
            if lst[k][i] != lst[k+1][i]:
                cnt_column = 0
            cnt_column += 1
            cnt_lst.append(cnt_column)
    return max(cnt_lst)    
n = int(input())
lst = []
for i in range(n):
    lst.append(list(input()))
cnt_lst = []
for i in range(len(lst)-1):
    for k in range(len(lst)-1):
        if k == (len(lst)-2):
            if lst[i][k+1] != lst[i+1][k+1]:
                lst[i][k+1],lst[i+1][k+1] = lst[i+1][k+1],lst[i][k+1]
                cnt_lst.append(test(lst))
                lst[i][k+1],lst[i+1][k+1] = lst[i+1][k+1],lst[i][k+1]
        if i == (len(lst)-2):
            if lst[i+1][k] != lst[i+1][k+1]:
                lst[i+1][k],lst[i+1][k+1] = lst[i+1][k+1],lst[i+1][k]
                cnt_lst.append(test(lst))
                lst[i+1][k],lst[i+1][k+1] = lst[i+1][k+1],lst[i+1][k]    
        if lst[i][k] != lst[i][k+1]:
            lst[i][k],lst[i][k+1] = lst[i][k+1],lst[i][k]
            cnt_lst.append(test(lst))
            lst[i][k],lst[i][k+1] = lst[i][k+1],lst[i][k]
        if lst[i][k] != lst[i+1][k]:
            lst[i][k],lst[i+1][k] = lst[i+1][k],lst[i][k]
            cnt_lst.append(test(lst))
            lst[i][k],lst[i+1][k] = lst[i+1][k],lst[i][k]
print(max(cnt_lst))
