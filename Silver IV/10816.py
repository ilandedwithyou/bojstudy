N = int(input())
A = list(map(int, input().split()))
A.sort()

M = int(input())
B = list(map(int, input().split()))

def lowerbound(A, b):
    start = 0
    end = len(A)

    while(start < end):
        mid = (start + end) // 2
        if(A[mid] < b):
            start = mid + 1
        else:
            end = mid
        
    return start

def upperbound(A, b):
    start = 0
    end = len(A)

    while(start < end):
        mid = (start + end) // 2

        if(A[mid] <= b):
            start = mid + 1
        else:
            end = mid
    return start




for b in B:
    print(upperbound(A, b) - lowerbound(A, b), end = ' ')