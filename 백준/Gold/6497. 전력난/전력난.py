'''
https://www.acmicpc.net/problem/6497
전력난
'''
import sys
input = sys.stdin.readline

def solution(M, N) :

    edges = []
    parent = [v for v in range(M+1)]
    totalCost = 0
    minCost = 0
    count = 0
    for _ in range(N) :
        x, y, z = map(int, input().rstrip().split())
        totalCost += z
        edges.append((z, x, y))

    edges.sort()


    def getRootParent(v) :
        if v == parent[v] :
            return v
        parent[v] = getRootParent(parent[v])
        return parent[v]
    def unionParent(v1, v2) :
        v1 = getRootParent(v1)
        v2 = getRootParent(v2)
        parent[v2] = v1


    for len, v1, v2 in edges :
        if getRootParent(v1) == getRootParent(v2) :
            continue
        minCost += len
        count += 1
        unionParent(v1, v2)
        if count == M-1 :
            break

    return totalCost - minCost

M, N = map(int, input().rstrip().split())
while M != 0 and N != 0 :
    print(solution(M, N))
    M, N = map(int, input().rstrip().split())