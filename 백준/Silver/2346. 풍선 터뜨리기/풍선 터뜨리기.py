from collections import deque

n = int(input())
arr = deque(enumerate(map(int, input().split())))

for i in range(n):
    idx, val = arr.popleft()
    print(idx+1, end=' ')
    if val > 0:
        arr.rotate(-(val-1))
    else:
        arr.rotate(-val)