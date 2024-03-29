import sys
from collections import defaultdict
input = sys.stdin.readline
input()
graph = defaultdict(list)
for _ in range(int(input())) :
    s, e = map(int, input().rstrip().split(' '))
    graph[s].append(e)
    graph[e].append(s)
    
visited=[]
def dfs(startV) :
    visited.append(startV)
    for v in graph[startV] :
        if v not in visited :
            dfs(v)
    return len(visited)-1

print(dfs(1))