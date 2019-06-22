import sys

sys.setrecursionlimit(100000)

# n factorial
def fact(n: int):
    if (n == 0):
         return 1
    return n * fact(n-1)

# Fibonacci sequence
def fibo(n: int):
    if (n==1 or n==2):
        return 1
    return fibo(n-1) + fibo(n-2)

# Fibonacci sequence with memo
memo = [-1] * 100000
memo[0] = 1
memo[1] = 1
memo[2] = 1
def fibo_memo(n: int):
    if not(memo[n] == -1):
        return memo[n]
    else:
        memo[n] = fibo_memo(n-1) + fibo_memo(n-2)
        return memo[n]


if __name__ == "__main__":
    ans = fibo_memo(35)
    print(ans)