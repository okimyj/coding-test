'''
https://www.acmicpc.net/problem/4386
별자리 만들기
'''
import sys
from itertools import combinations
from math import sqrt
input = sys.stdin.readline
N = int(input())
vertexes = []
edges = []
parent = [v for v in range(N+1)]
def getParent(v) :
    if parent[v] == v :
        return v
    parent[v] = getParent(parent[v])
    return parent[v]
def unionParent(v1, v2) :
    v1 = getParent(v1)
    v2 = getParent(v2)
    parent[v2] = v1
def getDistance(v1, v2) :
    a = v1[1] - v2[1]
    b = v1[2] - v2[2]
    return sqrt((a*a) + (b*b))
def makeEdge(v1, v2) :
    return (getDistance(v1, v2), v1[0], v2[0])

for i in range(N) :
    x, y = map(float, input().rstrip().split())
    vertexes.append((i, x, y))

for v1, v2 in combinations(vertexes, 2) :
    edges.append(makeEdge(v1, v2))
edges.sort()

totalCost = 0
for dist, v1, v2 in edges :
    if getParent(v1) == getParent(v2) :
        continue
    totalCost += dist
    unionParent(v1, v2)

print(totalCost)