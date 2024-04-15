'''
https://www.acmicpc.net/problem/14621
나만 안되는 연애
제목이 ☆로 맘에 안듬 ^^
1. 같은 타입의 학교간의 연결 간선은 데이터에 추가하지 않는다.
2. 나머지 크루스칼 알고리즘 똑같.
3. 모두 순회 한 후 각 정점의 parent 비교.
'''
import sys
input = sys.stdin.readline

def getParent(v) :
    if parent[v] == v :
        return v
    parent[v] = getParent(parent[v])
    return parent[v]

def unionParent(v1, v2) :
    v1 = getParent(v1)
    v2 = getParent(v2)
    if v1 <= v2 :
        parent[v2] = v1
    else :
        parent[v1] = v2

N, M = map(int, input().rstrip().split())
schoolTypes = input().rstrip().split()
edges = []
parent = [v for v in range(N+1)]
for _ in range(M) :
    u, v, d = map(int, input().rstrip().split())
    if schoolTypes[u-1] != schoolTypes[v-1] :
        edges.append((u, v, d))
edges.sort(key=lambda x : x[2])

length = 0
for u, v, d in edges :
    if getParent(u) == getParent(v) :
        continue
    length+=d
    unionParent(u, v)

for i in range(1, N) :
    if getParent(i) != getParent(i+1) :
        print(-1)
        exit(0)

print(length)