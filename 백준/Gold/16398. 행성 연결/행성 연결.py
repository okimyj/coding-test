'''
https://www.acmicpc.net/problem/16398
행성 연결
edges : [(cost, start, end)]
'''
import sys
input = sys.stdin.readline
N = int(input())
edges = []
totalCost = 0
for s in range(1, N+1) :
    costs = list(map(int, input().rstrip().split()))
    for e in range(s, len(costs)) :
        edges.append((costs[e], s, e+1))
edges.sort()
parent = [x for x in range(N+1)]
def getParent(v) :
    if parent[v] == v :
        return v
    parent[v] = getParent(parent[v])
    return parent[v]

def unionParent(v1, v2) :
    v1 = getParent(v1)
    v2 = getParent(v2)
    parent[v2] = v1

for cost, v1, v2 in edges :
    if getParent(v1) == getParent(v2) :
        continue
    totalCost += cost
    unionParent(v1, v2)

print(totalCost)