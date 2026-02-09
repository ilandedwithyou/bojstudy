N = int(input())
nums = list(map(int, input().split()))

s = [-1]*(N)
idx = []

for i in range(N):
    current = nums[i]    

    while idx and nums[idx[-1]] < current:
        s[idx.pop()] = current

    idx.append(i)

print(*s)