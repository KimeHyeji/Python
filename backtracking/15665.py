def func(k):
    if k == M:
        for i in range(M):
            print(arr[i],end=' ')
        print()
        return 
    tmp = 0
    for i in num:
        if i != tmp:
            tmp = i
            arr[k] = i
            func(k+1)
N, M = map(int, input().split())
num = list(map(int,input().split()))
num.sort()
arr = [0] * M
func(0)