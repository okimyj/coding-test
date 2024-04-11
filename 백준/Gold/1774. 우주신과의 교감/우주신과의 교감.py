'''
https://www.acmicpc.net/problem/1774
우주신과의 교감
'''
import sys
from itertools import combinations
from math import sqrt
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
edges = []
vertexes = []
parent = [v for v in range(N+1)]
totalLen = 0
count = 0
def findRootParent(v) :
    if parent[v] == v :
        return v
    parent[v] = findRootParent(parent[v])
    return parent[v]
def unionParent(v1, v2) :
    v1 = findRootParent(v1)
    v2 = findRootParent(v2)
    if v1 < v2 :
        parent[v2] = v1
    else:
        parent[v1] = v2
def distance(v1, v2) :
    a = v1[1] - v2[1]
    b = v1[2] - v2[2]
    return sqrt(a*a + b*b)
def makeEdges(v1, v2) :
    return (distance(v1, v2), v1[0], v2[0])

for i in range(N) :
    X, Y = map(int, input().rstrip().split())
    vertexes.append((i+1, X, Y))

for i in range(M) :
    v1, v2 = map(int, input().rstrip().split())
    if findRootParent(v1) == findRootParent(v2) :
        continue
    unionParent(v1, v2)
    count += 1

for v1, v2 in combinations(vertexes, 2) :
    edges.append(makeEdges(v1, v2))

edges.sort()

for cost, v1, v2 in edges :
    if findRootParent(v1) == findRootParent(v2) :
        continue
    totalLen += cost
    count += 1
    unionParent(v1, v2)
    if count == N -1 :
        break

print(f"{totalLen:.2f}")