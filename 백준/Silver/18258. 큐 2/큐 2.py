import sys
from collections import deque
input = sys.stdin.readline
q = deque()
for _ in range(int(input())) :
    op = input().rstrip().split()
    if op[0] == 'push' :
        q.append(int(op[1]))
    elif op[0] == 'pop' :
        print(len(q) == 0 and -1 or q.popleft())
    elif op[0] == 'size' :
        print(len(q))
    elif op[0] == 'empty':
        print(len(q) == 0 and 1 or 0)
    elif op[0] == 'front' :
        print(len(q) == 0 and -1 or q[0])
    elif op[0] == 'back':
        print(len(q) == 0 and -1 or q[len(q)-1])

