'''
https://www.acmicpc.net/problem/4386
별자리 만들기
'''
import sys
from math import sqrt
from itertools import combinations
input = sys.stdin.readline
N = int(input())
vertexes = []
edges = []
for i in range(N) :
    X, Y = map(float, input().rstrip().split())
    vertexes.append((i, X, Y))
def calcDist(x, y, x1, y1) :
    a = x - x1
    b = y - y1
    return sqrt((a*a) + (b*b))
def makeEdge(comb) :
    A = comb[0]
    B = comb[1]
    return (calcDist(A[1], A[2], B[1], B[2]), A[0], B[0])

for comb in combinations(vertexes, 2) :
    edge = makeEdge(comb)
    edges.append(makeEdge(comb))

edges.sort()

parent = [v for v in range(N+2)]
def findRootParent(v) :
    if v == parent[v] :
        return v
    parent[v] = findRootParent(parent[v])
    return parent[v]
def unionParent(v1, v2) :
    v1 = findRootParent(v1)
    v2 = findRootParent(v2)
    parent[v2] = v1

totalCost = 0
count = 0
for cost, v1, v2 in edges :
    if findRootParent(v1) == findRootParent(v2) :
        continue
    totalCost += cost
    count += 1
    unionParent(v1, v2)
    if count == N :
        break

print(totalCost)