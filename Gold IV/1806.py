N,S  = map(int, input().split())
ll = list(map(int, input().split()))

start = 0
sums = 0
answer = N + 1

for end in range(N):
    sums = sums+ ll[end]

    while sums >= S:
        answer = min(answer, end-start+1)
        sums -= ll[start]
        start += 1
if answer == N + 1:
    print(0)
else:
    print(answer)
