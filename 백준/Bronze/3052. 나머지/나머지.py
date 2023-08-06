lst = []
for i in range(10):
    lst.append(int(input()))

for i in range(10):
    lst[i] = lst[i]%42

lst2 = []
for i in lst:
    if i not in lst2:
        lst2.append(i)

print(len(lst2))
