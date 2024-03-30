# W가 내 팀, B가 상대 팀.
import sys
from collections import deque, defaultdict
input = sys.stdin.readline
cols, rows = map(int, input().rstrip().split())
_map = [list(input().rstrip()) for _ in range(rows)]
visited = [[False for _ in range(cols)] for _ in range(rows)]
power = defaultdict(list)
# power = {'W':[], 'B':[]}

def isInRange(r, c) :
    return r >= 0 and r < rows and c >= 0 and c < cols
def canVisit(r, c) :
    return isInRange(r, c) and not visited[r][c]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
def bfs(r, c, team) :
    q = deque([(r, c)])
    power[team][len(power[team]) - 1] += 1
    visited[r][c] = True
    while q :
        curR, curC = q.popleft()
        for i in range(4) :
            nextR = curR + dr[i]
            nextC = curC + dc[i]
            if canVisit(nextR, nextC) and _map[nextR][nextC] == team :
                q.append((nextR, nextC))
                power[team][len(power[team])-1] += 1
                visited[nextR][nextC] = True

for r in range(rows) :
    for c in range(cols):
        if canVisit(r, c) :
            power[_map[r][c]].append(0)
            bfs(r, c, _map[r][c])

print(sum([x**2 for x in power['W']]), end=' ')
print(sum([x**2 for x in power['B']]))