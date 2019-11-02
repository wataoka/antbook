def bellman_ford(edges:list, num_v:int, source:int):
    INF = float("inf")
    d = [INF]*(num_v)
    d[source] = 0
    for i in range(num_v):
        for edge in edges:
            f, t, c = edge
            if f!=INF and d[t]>d[f]+c:
                d[t] = d[f]+c
                if i==num_v-1:
                    return -1
    return d