'''
1417 국회의원 선거
'''
import sys
from heapq import heapify, heappop, heappush
input = sys.stdin.readline
N = int(input())
me = int(input())
buy = 0
votes = [int(input())*-1 for _ in range(N-1)]
if N == 1 :
    print(0)
    exit(0)
heapify(votes)
while votes[0] <= -(me+buy) :
    v = heappop(votes)+1
    heappush(votes, v)
    buy += 1

print(buy)