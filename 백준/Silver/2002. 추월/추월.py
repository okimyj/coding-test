import sys
from collections import deque
input = sys.stdin.readline
carNum = int(input())

inQ = deque([input().rstrip() for i in range(carNum)])
outQ = deque([input().rstrip() for i in range(carNum)])
count = 0
while outQ :
    out = outQ.popleft()
    if inQ[0] == out :
        inQ.popleft()
    else:
        inQ.remove(out)
        count += 1

print(count)