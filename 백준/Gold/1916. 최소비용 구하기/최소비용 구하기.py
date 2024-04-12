'''
https://www.acmicpc.net/problem/1916
최소 비용 구하기
'''
import sys
from heapq import heappop, heappush
input = sys.stdin.readline
N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
times = [100000*N for _ in range(N+1)]
for _ in range(M) :
    start, end, time = map(int, input().rstrip().split())
    graph[start].append((end, time))

S, E = map(int, input().rstrip().split())

pq = []
times[S] = 0
heappush(pq, (times[S], S))
while pq :
    curTime, cur = heappop(pq)
    if cur == E :
        print(curTime)
        exit(0)

    for end, time in graph[cur] :
        nextTime = curTime + time
        if nextTime < times[end] :
            times[end] = nextTime
            heappush(pq, (nextTime, end))

