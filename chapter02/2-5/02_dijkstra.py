"""
ダイクストラ法

Params:
    s: 始点
    num_v: 頂点の数
    cost[u][v]: 辺uvのコスト (存在しない場合はINF)
Return:
    始点sから各頂点への最短距離リスト
"""

def dijkstra(s:int, num_v:int, cost):
    d = float("inf")*num_v
    used = [False]*num_v
    d[s] = 0
    while True:
        v = -1
        for i in range(num_v):
            if not(used[i]):
                if (v==-1) or (d[i]<d[v]):
                    v = i
        if v == -1:
            break
        used[v] = True

        for i in range(num_v):
            d[i] = min(d[i], d[v]+cost[v][i])
    return d
