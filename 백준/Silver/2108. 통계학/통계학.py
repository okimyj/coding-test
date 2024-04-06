'''
https://www.acmicpc.net/problem/2108
통계학
'''
import sys
from collections import defaultdict
input = sys.stdin.readline
N = int(input())
numbers = [int(input()) for _ in range(N)]
numbers.sort()
# 산술평균
print(round(sum(numbers) / N))
# 중앙 값
print(numbers[len(numbers)//2])
# 최빈 값
countDict = defaultdict(int)
for n in numbers :
    countDict[n] += 1
countDict = sorted(countDict.items(), key=lambda x:(-x[1], x[0]))
if len(countDict) > 1 and countDict[0][1] == countDict[1][1] :
    print(countDict[1][0])
else:
    print(countDict[0][0])
# 범위
print(numbers[len(numbers)-1] - numbers[0])