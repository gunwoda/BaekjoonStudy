n = int(input())
count = 0
if n<10:
    num = '0'+str(n)
else :
    num = str(n)
while True:
    count += 1
    new_num1 = str(int(num[0])+int(num[1]))
    new_num2 = int(num[1]+new_num1[-1])
    if new_num2 == n:
        break
    if new_num2 <10:
        new_num2 = '0'+str(num)
    num = str(new_num2)
    
print(count)
