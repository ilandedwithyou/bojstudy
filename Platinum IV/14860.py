import sys
input = sys.stdin.readline

MOD = 1_000_000_007

N, M = map(int, input().split())
L = min(N, M)

def getPhi(n):
    phi = [i for i in range(n + 1)] 

    for i in range(2, n + 1):
        if phi[i] == i:
            for j in range(i, n + 1, i):
                phi[j] -= phi[j] // i

    return phi

phi = getPhi(L)

answer = 1

for d in range(1, L + 1):
    nd = N // d
    md = M // d
    limit = min(nd, md)

    cnt = 0
    for k in range(1, limit + 1):
        cnt += phi[k] * (nd // k) * (md // k)

    answer = answer * pow(d, cnt, MOD) % MOD

print(answer)
