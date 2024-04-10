'''
https://www.acmicpc.net/problem/1922
네트워크 연결
'''
import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
edges = []
for _ in range(M) :
    A, B, W = map(int, input().rstrip().split())
    edges.append((W, A, B))

edges.sort()

parent = [v for v in range(N+1)]
def findParent(v) :
    if parent[v] == v :
        return v
    parent[v] = findParent(parent[v])
    return parent[v]

def unionParent(v1, v2) :
    v1 = findParent(v1)
    v2 = findParent(v2)
    parent[v2] = v1

cost = 0
count = 0
for weight, v1, v2 in edges :
    if findParent(v1) == findParent(v2) :
        continue

    cost += weight
    count +=1
    unionParent(v1, v2)
    if count == N-1 :
        break
print(cost)
