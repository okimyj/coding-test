'''
https://www.acmicpc.net/problem/11722
가장 긴 감소하는 부분 수열
'''
import sys
input = sys.stdin.readline
N = int(input())
numbers = list(map(int, input().rstrip().split()))
dp = [1]*N
for i in range(N) :
    for j in range(i) :

        if numbers[i] < numbers[j] :
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))