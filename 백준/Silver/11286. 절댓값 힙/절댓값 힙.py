'''
절댓값 힙
[접근]
- 힙에 튜플 형태로 데이터를 넣어주면 튜플의 첫번째 값을 기준으로 힙을 구성한다.
- 이를 이용해 첫번째 튜플의 값을 절대값으로, 두번째 값을 원래 값으로 구성한다.
- 절댓값이 가장 작은 값이 여러개인 경우

'''
import sys
from heapq import heapify, heappop, heappush
input = sys.stdin.readline
numbers = []
for _ in range(int(input())) :
    op = int(input())
    if op == 0 :
        if len(numbers) == 0 :
            print(0)
        else:
            minV = heappop(numbers)
            print(minV[1])
    else :
        heappush(numbers, (abs(op), op))