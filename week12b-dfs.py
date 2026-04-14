g = {
    0: [1, 2],
    1: [0, 3, 2],
    2: [3, 4],
    3: [1, 2],
    4: [2]
}

v = set()

def dfs(v, g, n):
    if n not in v:
        v.add(n)
        print(n, end=" ")
        for i in g[n]:
            dfs(v, g, i)

dfs(v, g, 0)