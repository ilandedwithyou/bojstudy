N, M, L = map(int, input().split())
rests = list(map(int ,input().split()))

rests.append(0)
rests.append(L)

rests.sort()

start = 1
end = 0
for i in range(1, N+2):
    end = max(end, rests[i] - rests[i-1])

while (start <= end):
    mid = (start + end ) // 2

    cnt = 0
    for i in range(1, N+2):
        temp = rests[i]-rests[i-1]

        cnt = cnt + ((temp-1) // mid)
        
    if(cnt > M):
        start = mid + 1
    else:
        end = mid - 1

print(end+1)