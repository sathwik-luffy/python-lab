g = {
    0: [1, 2],
    1: [0, 3, 2],
    2: [0, 3, 4],
    3: [1, 2],
    4: [2]
}

v = []
q = []

def bfs(v, g, n):
    v.append(n)
    q.append(n)
    while(q):
        s = q.pop(0)
        print(s, end=" ")
        for i in g[s]:
            if i not in v:
                v.append(i)
                q.append(i)

bfs(v, g, 0)