# num_v:頂点の数, num_e:辺の数
num_v, num_e = map(int, input().split())

# g[i]: 点iに隣接している点のリスト
g = [[] for i in range(num_v)]

for i in range(num_e):
    x, y = map(int, input().split())
    g[x].append(y)
    g[y].append(x)

# color[i]: 点iの色 (1 or -1) (塗られていないときは0)
color = [0]*num_v

# 頂点vを色cで塗り, 成り立つかどうかの判定
def dfs(v:int, c:int):
    color[v] = c
    for next_v in g[v]:
        if color[next_v] == c:
            return False
        if color[next_v] == 0:
            if not dfs(next_v, -c):
                return False
    return True

def solve():
    for vi in range(num_v):
        if color[vi] == 0:
            if not dfs(vi, 1):
                return "No"
    return "Yes"

res = solve()
print(res)