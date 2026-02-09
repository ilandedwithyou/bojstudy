import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
A.append(0)
A.append(0)

cost = 0

for i in range(N):
    if A[i+1] > A[i+2]:
        two = min(A[i], A[i+1] - A[i+2])
        A[i] -= two
        A[i+1] -= two
        cost += 5 * two

    three = min(A[i], A[i+1], A[i+2])
    A[i] -= three
    A[i+1] -= three
    A[i+2] -= three
    cost += 7 * three

    cost += 3 * A[i]

print(cost)