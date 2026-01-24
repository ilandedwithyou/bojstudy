import sys
input = sys.stdin.readline

N = int(input())

dp = [0] * (N + 1)

squares = []
k = 1
while k * k <= N:
    squares.append(k * k)
    k += 1

for i in range(1, N + 1):
    dp[i] = i
    for sq in squares:
        if sq > i:
            break
        dp[i] = min(dp[i], dp[i - sq] + 1)

print(dp[N])
