'''
https://www.acmicpc.net/problem/7562
나이트의 이동
'''
import sys
from collections import deque
input = sys.stdin.readline

dr = [2, 2, -2, -2, 1, 1, -1, -1]
dc = [-1, 1, -1, 1, 2, -2, 2, -2]

def checkMoveCount() :
    L = int(input())
    def isInRange(r, c) :
        return r >= 0 and r < L and c >= 0 and c < L

    visited = [[False]*L for _ in range(L)]
    startR, startC = map(int, input().rstrip().split())
    targetR, targetC = map(int, input().rstrip().split())
    q = deque([(startR, startC)])
    visited[startR][startC] = 0
    while q :
        curR, curC = q.popleft()
        if curR == targetR and curC == targetC :
            return visited[targetR][targetC]
        for i in range(8) :
            nextR = curR + dr[i]
            nextC = curC + dc[i]
            if isInRange(nextR, nextC) and visited[nextR][nextC] == False :
                visited[nextR][nextC] = visited[curR][curC] + 1
                q.append((nextR, nextC))
    return 0

for _ in range(int(input())) :
    print(checkMoveCount())
