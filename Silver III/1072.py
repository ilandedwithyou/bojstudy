X, Y = map(int, input().split())

start = 1
end = 1_000_000_000
Z = (Y * 100) // X
answer = -1

if Z >= 99:
    print(-1)
else:
    while(start <= end):
        mid = (start + end) // 2
        tempZ = ((Y + mid) * 100) // (X + mid)

        if tempZ > Z:
            answer = mid
            end = mid - 1 
        else:
            start = mid + 1

    print(answer)