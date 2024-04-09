'''
https://www.acmicpc.net/problem/13975
파일 합치기3
작은 파일 부터 순서대로 합친다.
'''
import sys
from heapq import heappop, heappush, heapify
input = sys.stdin.readline
for _ in range(int(input())) :
    input() # 파일 갯수
    files = list(map(int, input().rstrip().split()))
    heapify(files)
    result = 0
    while len(files) > 1 :
        sum = heappop(files) + heappop(files)
        result += sum
        heappush(files, sum)
    print(result)