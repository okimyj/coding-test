import sys
from collections import deque
inputCount = int(sys.stdin.readline())
q = deque()
for i in range(inputCount) :
    number = int(sys.stdin.readline())
    if number == 0 :
        q.pop()
    else :
        q.append(number)
print(sum(list(q)))