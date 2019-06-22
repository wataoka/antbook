import sys

n = int(input())
a = list(map(int, input().split()))
k = int(input())

def dfs(i, sum):
    # When dfs decides n times, dfs return whether sum equal to k.
    if (i==n):
        return sum == k
    
    # dfs don't use a[i].
    if (dfs(i+1, sum)):
        return True

    # dfs use a[i].
    if (dfs(i+1, sum+a[i])):
        return True

    # because dfs can't find solution in all cases.
    return False

def solve():
    if (dfs(0, 0)):
        print('Yes')
    else:
        print('No')



if __name__ == "__main__":
    solve()