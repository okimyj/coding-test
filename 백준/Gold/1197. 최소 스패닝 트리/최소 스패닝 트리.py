'''
https://www.acmicpc.net/problem/1197
최소 스패닝 트리
크루스칼 알고리즘 : 그리디 알고리즘을 통해 최소 스패닝 트리를 구하는 알고리즘.
1. 선택되지 않은 간선들 중 최소 가중치인 간선을 선택.
2. 그 간선을 선택 했을 때 지금까지 구성된 스패닝 트리에 사이클이 없는 경우에만 선택 확정
    2-1. 해당 간선의 두 정점이 같은 최상위 parent 를 갖는다 = 사이클 발생.
3. 총 V-1 (정점개수 -1)개의 간선이 선택될 때 까지 반복.
'''
import sys
from heapq import heappop, heappush
input = sys.stdin.readline
V, E = map(int, input().rstrip().split())
parent = [v for v in range(V+1)]
graph = []

for _ in range(E) :
    A, B, C = map(int, input().rstrip().split())
    graph.append((C, A, B))

# 첫번째 값 가중치를 기준으로 정렬)
graph.sort()
def findRoot(v) :
    if parent[v] == v :
        return v
    parent[v] = findRoot(parent[v])         # 경로 압축.
    return parent[v]

def unionRoot(v1, v2) :
    v1 = findRoot(v1)
    v2 = findRoot(v2)
    if v1 != v2 :
        parent[v2] = v1

answer = 0
cnt =0
for weight, v1, v2 in graph :

    if findRoot(v1) == findRoot(v2) :
        continue

    answer+=weight
    unionRoot(v1, v2)
    cnt+=1
    if cnt == V-1 :
        break

print(answer)