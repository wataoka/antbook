N = int(input())
w = []
v = []
for i in range(N):
    w_i, v_i = map(int, input().split())
    w.append(w_i)
    v.append(v_i)
W = int(input())

# dp[i][j]は重さjまで入れていい状況においてi番目までの最適なvalueを保証している。
dp = [[0]*(W+1) for i in range(N+1)]

for i in range(N):
    for j in range(W+1):
        if w[i] > j:
            dp[i+1][j] = dp[i][j]
        else:
            dp[i+1][j] = max(dp[i][j], dp[i][j-w[i]]+v[i])

print(dp[-1][-1])
