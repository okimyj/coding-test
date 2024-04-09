'''
https://www.acmicpc.net/problem/1697
숨바꼭질
'''
import sys
from collections import deque
input = sys.stdin.readline
N, K = map(int, input().rstrip().split())

q = deque([(N, 0)])
visited = [False for _ in range(100001)]
visited[N] = True
def canVisit (x) :
    return x >= 0 and x < 100001 and not visited[x]


while q :
    curX, curSec = q.popleft()
    if curX == K :
        print(curSec)
        exit(0)
    if canVisit(curX+1) :
        visited[curX+1] = True
        q.append((curX+1, curSec+1))
    if canVisit(curX-1) :
        visited[curX-1] = True
        q.append((curX-1, curSec+1))
    if canVisit(curX*2) :
        visited[curX*2] = True
        q.append((curX*2, curSec+1))


