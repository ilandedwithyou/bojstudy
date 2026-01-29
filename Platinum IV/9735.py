N = int(input())

def findInt(a, b, c, d):
    def f(x):
        return a*(x**3) + b*(x**2) + c*x + d
    
    if f(0) == 0: return 0
    for x in range(1, 2000001):
        if f(x) == 0: return x
        if f(-x) == 0: return -x
    return None

def findtwo(a, b, c):
    d = b**2 - (4 * a * c)

    if(d < 0):
        return []
    elif(d == 0):
        return [-b/(2*a)]
    else:
        return [(-b + d**0.5) / (2*a), (-b - d**0.5) / (2*a)]

for _ in range(N):
    a, b, c, d = map(int, input().split())

    r = findInt(a, b, c, d)
    roots = [float(r)]

    A2 = a
    B2 = b + a * r
    C2 = c + B2 * r

    roots += findtwo(A2, B2, C2)

    roots = sorted(set(roots))

    print(" ".join(f"{x:.4f}" for x in roots))
