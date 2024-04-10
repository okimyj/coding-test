'''
https://www.acmicpc.net/problem/2805
binary_search 나무자르기
'''
import sys
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
lengths = list(map(int, input().rstrip().split()))

start = 1
end = max(lengths)
answer = 0
while start <= end :
    mid = (start + end) // 2

    total = 0
    for len in lengths :
        if len > mid :
            total += len - mid
    
    # 필요한 길이 보다 크거나 같다. 절단기의 높이를 올려준다.
    if M <= total :
        answer = mid
        start = mid +1
    else :
        end = mid -1




print(answer)