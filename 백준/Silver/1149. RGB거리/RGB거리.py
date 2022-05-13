N = int(input())

dp = []
for _ in range(N):
    dp.append(list(map(int, input().split())))
    
for index in range(1, len(dp)):
    dp[index][0] = min(dp[index-1][1],dp[index-1][2])+dp[index][0]
    dp[index][1] = min(dp[index-1][0],dp[index-1][2])+dp[index][1]
    dp[index][2] = min(dp[index-1][0],dp[index-1][1])+dp[index][2]
    
print(min(dp[N-1][0], dp[N-1][1], dp[N-1][2]))