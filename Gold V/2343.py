N, M = map(int, input().split())

blues = list(map(int, input().split()))

start = max(blues)
end = sum(blues)

while(start <= end):
    mid = (start+end)//2

    temp = 0
    cnt = 1
    for blue in blues:
        if(temp + blue <= mid):
            temp += blue
        else:
            cnt = cnt + 1
            temp = blue

    if(cnt <= M):
        end = mid - 1 
    else:
        start = mid + 1

print(start)