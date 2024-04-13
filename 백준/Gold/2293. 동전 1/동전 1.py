'''
https://www.acmicpc.net/problem/2293
동전 1
N : 동전 종류의 개수
K : 가치의 합 목표

----- coin = 1    dp[0] : 1
dp[1] = dp[1] + dp[1-coin(1)] = 1
           0       dp[0] : 1
dp[2] = dp[2] + dp[2-coin(1)] = 1
          0         dp[1] : 1
dp[3] = dp[3] + dp[3-coin(1)] = 1
          0         dp[2] : 1
dp[4] = dp[4] + dp[4-coint(1)] = 1
          0         dp[3] : 1
...
----- coin = 2
-- dp[1, 1, 1, 1, ...]
dp[2] = dp[2] + dp[2-coin(2)] = 2
        1          dp[0] : 1
-- dp[1, 1, 2, 1, ...]
dp[3] = dp[3] + dp[3-coin(2)] = 2
         1    +    dp[1] : 1
-- dp[1, 1, 2, 3, ...]
dp[4] = dp[4] + dp[4-coin(2)] = 3
         1         dp[2] : 2
'''
import sys
input = sys.stdin.readline
N, K = map(int, input().rstrip().split())
coins = [int(input()) for _ in range(N)]
dp = [0 for _ in range(K+1)]
dp[0] = 1

for coin in coins :
    for i in range(coin, K+1) :
        dp[i] = dp[i] + dp[i - coin]

print(dp[K])