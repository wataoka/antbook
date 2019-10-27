"""
LCS: Longest Common Subsequence (最長共通部分列)

dp[i+1][j+1]: s1...siとt1...tjに対するLCSの長さ
(本には、dp[i][j]と書かれているが、dp[i+1][j+1]だと思う。)

s1...s(i+1)とt1...t(j+1)に対する共通部分列は、
    s(i+1)=t(j+1)ならば、
        s1...siとt1...tjに対する共通部分列の後ろにs(i+1)を繋げたもの
    s(i+1)!=t(j+1)ならば、
        s1...siとt1...t(j+1)に対する共通部分列
        s1...s(i+1)とt1...tjに対する共通部分列
のどれかである。
"""

n = int(input())
m = int(input())
s = list(input())
t = list(input())

dp = [[0]*(m+1) for i in range(n+1)]

for i in range(n):
    for j in range(m):
        if s[i]==t[j]:
            dp[i+1][j+1] = dp[i][j]+1
        else:
            dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

print(dp[-1][-1])