'''
https://www.acmicpc.net/problem/2178
미로탐색
1 : 땅
0 : 벽
'''
import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
graph = [list(input().rstrip()) for _ in range(N)]

visited = [[False] * M for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

q = deque([(0, 0, 1)])
visited[0][0] =  True
def isInRange(x, y) :
    return x >= 0 and x < M and y >= 0 and y < N
answer = 0
while q:
    curX, curY, curC = q.popleft()

    if curX == M-1 and curY == N-1 :
        answer = curC
        break
    for i in range(4) :
        nextX = curX + dx[i]
        nextY = curY + dy[i]
        if isInRange(nextX, nextY) and not visited[nextY][nextX] and graph[nextY][nextX] == '1':
            visited[nextY][nextX] = True
            q.append((nextX, nextY, curC +1))


print(answer)