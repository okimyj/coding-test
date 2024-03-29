import sys
from collections import defaultdict
input = sys.stdin.readline
input()
graph = defaultdict(list)
for _ in range(int(input())) :
    s, e = map(int, input().rstrip().split(' '))
    graph[s].append(e)
    graph[e].append(s)

# def dfs(cur=startV, visited=[]) :
#     visited.append(cur)
#     for v in graph[cur] :
#         if v not in visited :
#             visited = dfs(v, visited)
#     return visited

def dfs(startV, visited = []) :
    visited.append(startV)
    for v in graph[startV] :
        if v not in visited :
            visited = dfs(v, visited)
    return visited

print(len(dfs(1))-1)