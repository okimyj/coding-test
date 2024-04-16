'''
https://www.acmicpc.net/problem/10282
해킹
'''
import sys
from heapq import heappop, heappush
input = sys.stdin.readline
for _ in range(int(input())) :
    n, d, c = map(int, input().rstrip().split())
    graph = [[] for _ in range(n+1)]
    visited = [sys.maxsize] * (n+1)
    for _ in range(d) :
        a, b, s = map(int, input().rstrip().split())
        graph[b].append((a, s))

    pq = []
    heappush(pq, (0, c))
    visited[c] = 0
    count = 1
    while pq :
        curSec, cur = heappop(pq)
        for target, sec in graph[cur] :
            nextSec = curSec + sec
            if visited[target] > curSec+sec :
                visited[target] = nextSec
                heappush(pq, (nextSec, target))

    filtered = list(filter(lambda x : x != sys.maxsize, visited))
    print(len(filtered), max(filtered))
