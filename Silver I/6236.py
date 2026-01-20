N, M = map(int, input().split())
moneys = [int(input()) for _ in range (N)]

start = max(moneys)
end = sum(moneys)

while(start <= end):
    mid = (start + end) // 2

    temp = mid
    cnt = 1
    for money in moneys:
        if(temp < money):
            cnt = cnt + 1
            temp = mid
        temp = temp - money

    if(cnt <= M):
        end = mid - 1
    else:
        start = mid + 1

print(start)