n, m = map(int, input().split())
field = []
for i in range(n):
    field.append(list(input()))

def dfs(x, y):
    field[x][y] = '.'

    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]: 
            if not((dx, dy) == (0, 0)):
                next_x, next_y = x+dx, y+dy
                if (0 <= next_x and next_x < n) and (0 <= next_y and next_y < m):
                    if (field[next_x][next_y] == 'W'):
                        dfs(next_x, next_y)

def solve():
    res = 0
    for i in range(n):
        for j in range(m):
            if (field[i][j] == 'W'):
                dfs(i, j)
                res += 1

    print(res)

if __name__ == "__main__":
    solve()