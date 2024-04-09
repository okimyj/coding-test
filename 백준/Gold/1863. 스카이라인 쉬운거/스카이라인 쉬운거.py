'''
https://www.acmicpc.net/problem/1863
스카이라인
'''
import sys
input = sys.stdin.readline
N = int(input())
heights = []

for i in range(N):
    X, Y = map(int, input().rstrip().split())
    heights.append(Y)
heights.append(0)

cnt = 0
curH = 0
checkStack = [0]
for h in heights :
    curH = h
    while checkStack and checkStack[-1] > h :
        # 다른 높이의 지점이 나오면 건물이 끝났다. curH 갱신
        if checkStack[-1] != curH :
            cnt +=1
            curH = checkStack[-1]
        checkStack.pop()
    checkStack.append(h)
print(cnt)

