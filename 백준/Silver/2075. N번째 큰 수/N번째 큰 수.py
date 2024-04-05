'''
2075 N번째 큰 수

'''
import sys
from heapq import heappop, heappush
input = sys.stdin.readline
N = int(input())
numbers = []
for _ in range(N) :
    for n in list(map(int, input().rstrip().split())) :
        if len(numbers) == N :
            if numbers[0] < n :
                heappop(numbers)
                heappush(numbers, n)
        else :
            heappush(numbers, n)


print(heappop(numbers))
