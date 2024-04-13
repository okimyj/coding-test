'''
https://www.acmicpc.net/problem/9084
동전
동전 1을 먼저 풀어서.. 같은데?

'''
import sys
input = sys.stdin.readline
for _ in range(int(input())) :
    input()
    coins = list(map(int, input().rstrip().split()))
    target = int(input())
    dp = [0 for _ in range(target+1)]
    dp[0] = 1
    for coin in coins :
        for i in range(coin, target+1) :
            dp[i] = dp[i] + dp[i-coin]

    print(dp[target])
