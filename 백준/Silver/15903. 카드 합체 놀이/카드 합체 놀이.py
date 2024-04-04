'''
1. 최소 힙을 사용해서 앞의 2개의 값을 뽑아내고, 더한 값을 2번 append
2. M번 반복 후 결과 값 출력.
'''
import sys
from heapq import heapify, heappush, heappop
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
cards = list(map(int, input().rstrip().split()))
heapify(cards)
for _ in range(M) :
    n = heappop(cards) + heappop(cards)
    heappush(cards, n)
    heappush(cards, n)

print(sum(cards))
