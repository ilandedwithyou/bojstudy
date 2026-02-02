n, m = map(int, input().split())
money = list(map(int, input().split()))

cur = sum(money[:m])
ans = cur

for i in range(m, n):
    cur = cur + money[i] - money[i-m]
    ans = max(cur, ans)

print (ans)