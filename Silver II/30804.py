N = int(input())
tanghuru = list(map(int, input().split()))

start = 0
count = [0]*(10)
kind = 0
answer = 0

for end in range(N):
    if(count[tanghuru[end]] == 0):
        kind += 1

    count[tanghuru[end]] += 1

    while kind > 2:
        count[tanghuru[start]] -= 1
        if count[tanghuru[start]] == 0:
            kind -= 1
        start += 1

    answer = max(answer, end - start + 1)

print(answer)