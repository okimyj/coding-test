'''
https://www.acmicpc.net/problem/1926
그래프 - 그림
'''
import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
graph = [input().rstrip().split() for _ in range(N)]
# print(*graph, sep='\n')

q = deque()
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
def isInRange(r, c) :
    return r >= 0 and r < N and c >= 0 and c < M

area = []
for r in range(N) :
    for c in range(M) :
        if graph[r][c] == '1' :
            q = deque([(r, c)])
            graph[r][c] = '0'
            areaNum = 1
            while q :
                curR, curC = q.popleft()
                for i in range(4) :
                    nextR = curR + dr[i]
                    nextC = curC + dc[i]
                    if isInRange(nextR, nextC) and graph[nextR][nextC] == '1' :
                        graph[nextR][nextC] = '0'
                        q.append((nextR, nextC))
                        areaNum += 1
            area.append(areaNum)

if len(area) == 0 :
    print(0, 0, sep='\n')
else:
    print(len(area), max(area), sep='\n')