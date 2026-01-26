N = int(input())
moneys = list(map(int, input().split()))
totalbuget = int(input())

start = 0
end = max(moneys)

while (start <= end):
    mid = (start + end)//2

    total = 0
    for money in moneys:
        total += min(money, mid)

    if total <= totalbuget:
        start = mid + 1
    else:
        end = mid - 1

print(end)