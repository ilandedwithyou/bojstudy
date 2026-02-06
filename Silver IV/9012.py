N = int(input())


def f(x):
    l = len(x)
    c = []
    for i in range(l):
        if(x[i] == '('):
            c.append(1)
        else:
            if(len(c) == 0):
                return 0
            c.pop()
    if(len(c) == 0):
        return 1
    else:
        return 0

for _ in range(N):
    s = input()

    if(f(s) == 1):
        print("YES")
    else:
        print("NO")

