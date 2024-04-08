'''
https://www.acmicpc.net/problem/16928
뱀과 사다리 게임
이 게임이 뭔질 모름 ^^...
뱀을 피해서 최대한 사다리 타고 이동해야하는 듯?....... 맞나...
'''
import sys
from collections import deque

input = sys.stdin.readline
ladderN, snakeN = map(int, input().rstrip().split())
_map = [0 for _ in range(101)]
for _ in range(ladderN) :
    s, e = map(int, input().rstrip().split())
    _map[s] = e

for _ in range(snakeN) :
    s, e = map(int, input().rstrip().split())
    _map[s] = e

visited = [False for _ in range(101)]

q = deque([1])
while q :
    cur = q.popleft()
    if cur == 100 :
        break
    for i in range(1, 6+1) :
        next = cur + i
        if next <= 100 and not visited[next] :
            if _map[next] :
                next = _map[next]
            if not visited[next] :
                visited[next] = visited[cur] + 1
                q.append(next)

print(visited[100])