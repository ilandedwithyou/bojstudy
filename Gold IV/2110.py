N, C = map(int, input().split())

lens=[]

for i in range(N):
    lens.append(int(input()))

lens.sort()
start = 1
end = lens[N-1]-lens[0]

while(start <= end):
    mid = (start + end) // 2

    cnt = 1
    temp = lens[0]
    for i in range (1, N):
        if(lens[i] - temp >= mid):
            cnt += 1
            temp = lens[i]
    
    if(cnt >= C):
        start = mid + 1
    else:
        end = mid -1

print(end)