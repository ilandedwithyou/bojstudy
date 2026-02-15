N = int(input())

dp=[1000000]*(N+1)

if(N >= 3):
    dp[3] =1
if(N >= 5):
    dp[5] = 1

for i in range(6, N+1):
    dp[i] = min(dp[i-3], dp[i-5]) + 1

print(dp[N])