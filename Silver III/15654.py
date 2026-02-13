N, M = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

visited = [False] * N
arr = []

def dfs():
    if len(arr) == M:
        print(*arr)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            arr.append(a[i])
            dfs()
            arr.pop()
            visited[i] = False

dfs()
