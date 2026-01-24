N, M = map(int, input().split())

times = [int(input()) for _ in range(N)]

start = 1
end = max(times)*M

while (start <= end):
    mid = (start + end) // 2

    totalTime = 0
    for time in times:
        totalTime = totalTime + (mid // time)

    if(totalTime >= M):
        end = mid - 1
    else:
        start = mid + 1

print(start)