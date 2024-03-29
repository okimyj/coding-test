import sys
from collections import deque, defaultdict
input = sys.stdin.readline

N, M, startV = map(int, input().split())  # 문자열을 정수형으로 변환

graph = defaultdict(list)  # defaultdict를 list로 초기화

# 그래프 생성
for _ in range(M):
    start, end = map(int, input().split())  # 문자열을 정수형으로 변환
    graph[start].append(end)
    graph[end].append(start)  # 양방향 간선 추가

# 각 노드의 인접한 노드 리스트를 정렬
for v in graph:
    graph[v].sort()

def dfs(cur, visited=[]):
    visited.append(cur)
    for v in graph[cur]:
        if v not in visited:
            visited = dfs(v, visited)
    return visited

def bfs():
    visited = [False] * (N + 1)
    result = []
    q = deque([startV])
    visited[startV] = True
    while q:
        cur = q.popleft()
        result.append(cur)
        for v in graph[cur]:
            if not visited[v]:
                visited[v] = True
                q.append(v)
    return result

print(*dfs(startV))
print(*bfs())