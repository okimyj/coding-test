'''
https://www.acmicpc.net/problem/1654
랜선 자르기
'''
import sys
input = sys.stdin.readline
K, N = map(int, input().rstrip().split())
lines = [int(input()) for _ in range(K)]

start = 1
end = 2**31-1
answer = 0
while start <= end :
    count = 0
    mid = (start+end) // 2
    for line in lines :
        count += line // mid

    if count >= N :
        start = mid+1
        answer = mid
    else :
        end = mid - 1


print(answer)