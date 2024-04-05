'''
3079 입국심사
풀이 봄..
'''
import sys
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
times = [int(input()) for _ in range(int(N))]
left = min(times)
right = max(times)*M
while left <= right :
    mid = (left+right)//2
    count = 0
    for i in range(N) :
        count += mid//times[i]

    if count < M :
        left = mid +1
    else:
        right = mid-1

print(left)