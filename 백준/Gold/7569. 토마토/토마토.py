'''
https://www.acmicpc.net/problem/7569
토마토

'''
import sys
from collections import deque
input = sys.stdin.readline
M, N, H = map(int, input().rstrip().split())
tomatos = []
q = deque()
unRipeNum = 0
for h in range(H) :
    tomatos.append([])
    for r in range(N) :
        line = list(map(int, input().rstrip().split()))
        tomatos[h].append(line)
        for i in range(len(line)) :
            if line[i] == 1 :
                q.append((h, r, i))
        unRipeNum += line.count(0)

visited = [[[False]*M for _ in range(N)] for _ in range(H)]

dr = [0, 1, 0, -1, 0, 0]
dc = [1, 0, -1, 0, 0, 0]
dh = [0, 0, 0, 0, 1, -1]
def isInRange(r, c, h) :
    return r >= 0 and r < N and c >= 0 and c < M and h >= 0 and h < H

needDays = -1
while q :
    curH, curR, curC = q.popleft()
    needDays = max(needDays, tomatos[curH][curR][curC])
    for i in range(6):
        nextR = curR + dr[i]
        nextC = curC + dc[i]
        nextH = curH + dh[i]
        if isInRange(nextR, nextC, nextH) and tomatos[nextH][nextR][nextC] == 0 and not visited[nextH][nextR][nextC]:
            visited[nextH][nextR][nextC] = True
            tomatos[nextH][nextR][nextC] = tomatos[curH][curR][curC] + 1
            q.append((nextH, nextR, nextC))
            unRipeNum -= 1


if unRipeNum :
    print(-1)
else:
    print(needDays-1)