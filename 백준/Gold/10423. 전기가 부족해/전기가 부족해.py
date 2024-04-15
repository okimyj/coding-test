'''
https://www.acmicpc.net/problem/10423
전기가 부족해
parent union 할 때 YNY인 쪽으로 union 처리.
연결 시킬 때 두 정점의 parent가 모두 YNY인지 확인하고 맞으면 pass.

'''
import sys
input = sys.stdin.readline
def getParent(v) :
    if parent[v] != v :
        parent[v] = getParent(parent[v])
    return parent[v]

def unionParent(v1, v2) :
    v1 = getParent(v1)
    v2 = getParent(v2)
    if isInYNY(v1) :
        parent[v2] = v1
    else :
        parent[v1] = v2
def isInYNY(v) :
    return getParent(v) in YNY

N, M, K = map(int, input().rstrip().split())
YNY = list(map(int, input().rstrip().split()))
edges = []
parent = [v for v in range(N+1)]
for _ in range(M) :
    a, b, c = map(int, input().rstrip().split())
    edges.append((a, b, c))

edges.sort(key=lambda x : x[2])

totalCost = 0
for a, b, c in edges :
    if (getParent(a) == getParent(b)) or (isInYNY(a) and isInYNY(b)) :
        continue
    totalCost += c
    unionParent(a, b)

print(totalCost)