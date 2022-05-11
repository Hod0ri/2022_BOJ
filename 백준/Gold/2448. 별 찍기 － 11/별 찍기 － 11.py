def rec(x, y, n):
    if n == 3:
        ans[x][y] = '*'
        ans[x+1][y-1] = ans[x+1][y+1] = '*'
        for i in range(-2, 3):
            ans[x+2][y+i] = '*'
    else:
        nn = n // 2
        rec(x, y, nn)
        rec(x+nn, y-nn, nn)
        rec(x+nn, y+nn, nn)


N = int(input())
ans = [[' '] * 2 * N for _ in range(N)]

rec(0, N-1, N)
for row in ans:
    print("".join(row))