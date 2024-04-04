'''
카드 정렬하기
그냥 적은 카드 순으로 두 묶음씩 합치면 되는거아닌가?..
'''
import sys
from heapq import heappop, heappush
input = sys.stdin.readline
cards = []
for _ in range(int(input())) :
    heappush(cards, int(input()))

result = 0
while len(cards) > 1 :
    s = heappop(cards)+heappop(cards)
    result += s
    heappush(cards, s)

print(result)
