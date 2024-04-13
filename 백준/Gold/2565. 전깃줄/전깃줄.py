'''
https://www.acmicpc.net/problem/2565
전깃줄
위에서 아래로 연결되는 개수,
아래서 위로 연결되는 개수 중 적은 개수를 끊으면... 안됨. 같은 인덱스로 갈 수도 있음.... ?
'''
import sys
input = sys.stdin.readline
N = int(input())
dp=[1] * (N)
numbers = [list(map(int, input().rstrip().split())) for _ in range(N)]
numbers.sort()
for i in range(N) :
    for j in range(i) :
        if numbers[i][1] > numbers[j][1] :
            dp[i] = max(dp[i], dp[j]+1)

print(N - max(dp))
