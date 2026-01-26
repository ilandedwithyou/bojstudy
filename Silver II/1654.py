N, K = map(int, input().split())
lens = [int(input()) for _ in range(N)]

start = 1
end = max(lens)

while(start <= end):
    mid = (start + end) // 2

    cnt = 0
    for l in lens:
        cnt += l // mid

        if(cnt >= K):
            break
    
    if(cnt >= K):
        start = mid + 1
    else:
        end = mid - 1

print(end)