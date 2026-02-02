N, K = map(int, input().split())
a = list(map(int, input().split()))
s = [0]*(N+1)

cur = sum(a[:K])
ans = cur

for i in range(K, N):
    cur = cur + a[i] - a[i-K]
    ans = max(ans, cur)

print(ans)