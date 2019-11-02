"""
01_knapsackと問題は同じで、制約条件においてwがデカイ版

制約:
1 <= n M= 100
1 <= wi <= 10**7
1 <= vi <= 100
1 <= W <= 10**9

dp[i+1][j]: i番目までの品物から価値の総和がjになるように選んだときの重さの総和の最小値
(そのような解が存在しない場合はINFとする)

i+1番目までの品物から価値の総和がjとなるように選ぶためには
    i番目までの品物から価値の総和がjとなるように選ぶ
    i番目までの品物から価値の総和がj-v[i+1]となるように選ぶ、i+1番目の品物を加える。
の二通りである。
"""

n = int(input())
w, v = [], []
for i in range(n):
    wi, vi = map(int, input().split()) 
    w.append(wi)
    v.append(vi)
W = int(input())

INF = 10**9+1
VI_MAX = 100
dp = [[INF]*(VI_MAX*n+1) for i in range(n+1)]
dp[0][0] = 0

for i in range(n):
    for j in range(VI_MAX*n+1):
        if j < v[i]:
            dp[i+1][j] = dp[i][j]
        else:
            dp[i+1][j] = min(dp[i][j], dp[i][j-v[i]]+w[i])

res = 0
for j in range(VI_MAX*n+1):
    if dp[n][j]<W:
        res = j
print(res)