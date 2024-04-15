'''
https://www.acmicpc.net/problem/13418
학교 탐방하기
0 : 오르막길
1 : 내리막길
'''
import sys
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())

def getCost(edges) :
    parent=[v for v in range(N+1)]
    def getParent(v) :
        if parent[v] != v:
            parent[v] = getParent(parent[v])
        return parent[v]
    def unionParent(v1, v2) :
        v1 = getParent(v1)
        v2 = getParent(v2)
        parent[v2] = v1

    downHillCnt = 0
    for a, b, c in edges :
        if getParent(a) == getParent(b) :
            continue
        downHillCnt += c
        unionParent(a, b)
    return (N-downHillCnt)**2

edges = []
for _ in range(M+1) :
    a, b, c = map(int, input().rstrip().split())
    edges.append((a, b, c))


edges.sort(key=lambda x:x[2])
maxCost = getCost(edges)

edges.sort(key=lambda x: x[2], reverse=True)
minCost = getCost(edges)
print(maxCost - minCost)