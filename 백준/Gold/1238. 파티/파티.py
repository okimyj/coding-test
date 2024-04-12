'''
https://www.acmicpc.net/problem/1238
파티
N : 학생 수 (마을마다 1명)
M : 도로 수
X : 마을 번호?
(시작 마을 번호, 끝 마을 번호, 시간(가중치))
설명을 예쁘게 써놨네
'''
import sys
from heapq import heappush, heappop
input = sys.stdin.readline
N, M, X = map(int, input().rstrip().split())
roads = [[] for _ in range(N+1)]
for _ in range(M) :
    start, end, time = map(int, input().rstrip().split())
    roads[start].append((end, time))

def dijkstra(start, end):
    pq = []
    times = [sys.maxsize] * (N+1)
    times[start] = 0
    heappush(pq, (0, start))
    while pq :
        curTime, cur = heappop(pq)
        if cur == end :
            return curTime
        for road in roads[cur] :
            nextTime = curTime + road[1]
            if nextTime < times[road[0]] :
                times[road[0]] = nextTime
                heappush(pq, (times[road[0]], road[0]))

maxTime = 0
for i in range(N) :
    maxTime = max(maxTime, dijkstra(i+1, X) + dijkstra(X, i+1))


print(maxTime)