while True:
    lst = list(map(int,input().split()))
    if lst[0] == 0:
        break
    n = lst[0]
    lst = lst[1:]
    ret_list = [0,0,0,0,0,0]
    def Fn(depth, idx):
        if depth == 6:
            print(str(ret_list).replace('[','').replace(']','').replace(',',''))
            return
        for jdx in range(idx, len(lst)):
            ret_list[depth] = lst[jdx]
            Fn(depth+1, jdx + 1)        
    Fn(0, 0)
    print()