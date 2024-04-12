'''
https://www.acmicpc.net/problem/2109
순회강연
아.. 단순히 해당 날짜에 가서 강의를 하면 되는걸로 생각하고 풀었었는데 예제는 맞고 틀림.
!! d(1 ≤ d ≤ 10,000)일 안에 와서 강연을 해 주면 !!
그렇다고 단순히 p, d 기준으로 정렬해서 day 누적하면서 뽑아내면..
앞의 p 보다 뒤에 날짜의 p가 훨씬 더 높은 경우 놓침
'''
import sys
from heapq import heappop, heappush
input = sys.stdin.readline
_list = []
for _ in range(int(input())) :
    p, d = map(int, input().rstrip().split())
    _list.append((p, d))
_list.sort(key=lambda  x : (x[1], -x[0]))

# 순회 pay 목록
rotation = []
for p, d in _list :
    dayDiff = len(rotation) - d +1
    if dayDiff > 0 :
        if p > sum(rotation[:dayDiff]):
            for _ in range(dayDiff) :
                heappop(rotation)
            heappush(rotation, p)
    else :
        heappush(rotation, p)

print(sum(rotation))
