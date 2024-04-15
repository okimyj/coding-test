'''
https://www.acmicpc.net/problem/14938
서강 그라운드
왜맞틀..
'''
import sys
from heapq import heappop, heappush
input = sys.stdin.readline

n, m, r = map(int, input().rstrip().split())
items = list(map(int, input().rstrip().split()))
items.insert(0, 0)
edges = [[] for _ in range(n+1)]
for _ in range(r) :
    a, b, l = map(int, input().rstrip().split())
    edges[a].append((b, l))
    edges[b].append((a, l))

for e in edges :
    e.sort(key=lambda x:x[1])

def getMaxItemNum(start):
    visited = [sys.maxsize] * (n+1)
    pq = [(0, start)]

    visited[start] = True
    while pq :
        curLen, curP = heappop(pq)
        for e, l in edges[curP] :
            nextL = curLen + l
            if nextL <= m and visited[e] > nextL:
                visited[e] = nextL
                heappush(pq, (nextL, e))

    gainNum = 0
    for i in range(1, len(visited)) :
        if visited[i] != sys.maxsize :
            gainNum+=items[i]
    return gainNum

maxNum = 0
for i in range(1, n+1) :
    maxNum = max(maxNum, getMaxItemNum(i))

print(maxNum)