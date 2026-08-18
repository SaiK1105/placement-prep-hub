import sys
input = sys.stdin.readline

MOD = 10**9 + 7

m, n = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(m)]

dp = [[0]*n for _ in range(m)]
dp[0][0] = 1

for i in range(m):
    for j in range(n):
        if grid[i][j] == 1:
            dp[i][j] = 0
            continue
        if i == 0 and j == 0:
            continue
        top = dp[i-1][j] if i > 0 else 0
        left = dp[i][j-1] if j > 0 else 0
        dp[i][j] = (top + left) % MOD

print(dp[m-1][n-1])
