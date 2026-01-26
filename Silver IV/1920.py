N = int(input())
a = list(map(int, input().split()))
a.sort()

M = int(input())
b = list(map(int, input().split()))

for bb in b:
    start = 0
    end = N-1

    isFind = 0
    while(start <= end):
        mid = (start + end)//2

        if(bb == a[mid]):
            isFind = 1
            break
        elif(bb < a[mid]):
            end = mid - 1
        else:
            start = mid +1

    print(isFind)