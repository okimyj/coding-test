'''
https://www.acmicpc.net/problem/1647
도시 분할 계획
'''
import sys
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
edges = []
for _ in range(M) :
    A, B, C = map(int, input().rstrip().split())
    edges.append((C, A, B))
edges.sort()

parent = [v for v in range(N+1)]
def findParent(v) :
    if v == parent[v] :
        return v
    parent[v] = findParent(parent[v])
    return parent[v]
def unionParent(v1, v2):
    v1 = findParent(v1)
    v2 = findParent(v2)
    parent[v2] = v1

totalCost = 0
lastCost = 0
edgeNum = 0
mst = []
for C, v1, v2 in edges :
    if findParent(v1)== findParent(v2):
        continue
    totalCost += C
    edgeNum+=1
    mst.append((C, v1, v2))
    unionParent(v1, v2)
    lastCost = C
    if edgeNum == N-1 :
        break


print(totalCost - lastCost)