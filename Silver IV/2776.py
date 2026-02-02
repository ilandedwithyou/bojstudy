import sys
input = sys.stdin.readline


T = int(input())

for _ in range(T):
    N = int(input())
    A = set(map(int, input().split()))

    M = int(input())
    B = list(map(int, input().split()))

    res = []
    for bb in B:
        if(bb in A):
            res.append('1')
        else:
            res.append('0')
    
    print('\n'.join(res))