n = int(input())
field = []
for i in range(n):
    field.append(list(input()))

def dfs(x, y):
    field[x][y] = '.'

    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]: 
            if not((dx, dy) == (0, 0)):
                next_x, next_y = x+dx, y+dy
                if (0 <= next_x and next_x < n) and (0 <= next_y and next_y < n):
                    if (field[next_x][next_y] == 'W'):
                        dfs(next_x, next_y)

def solve():
    res = 0