#탑
import sys
input = sys.stdin.readline
input()
# 1. 앞에서부터 뒤로가면서 자기 앞의 탑들을 대상으로
# 뒤에서 부터 돌면서 자기보다 높은 탑이 있다면 해당 인덱스 출력
# 시간초과
# top = list(map(int, input().rstrip().split()))
# maxTopIdx = 0
# for i in range(len(top)) :
#     receiver = 0
#     if top[i] > top[maxTopIdx] :
#         maxTopIdx = i
#     for j in range(i, max(0, maxTopIdx-1), -1) :
#         if top[i] < top[j] :
#             receiver = j+1
#             break
#     print(receiver, end = ' ')


# 2. 수신 가능한 탑을 갈아치운다?
top = [(x, i) for i, x in enumerate(map(int, input().rstrip().split()))]
from collections import deque
deployed = deque()
for v in top :
    receiver = 0
    while deployed :
        # print("deployed : " , deployed)
        if deployed[0][0] < v[0] :
            deployed.popleft()
        else :
            receiver = deployed[0][1]+1
            break

    deployed.appendleft(v)
    print(receiver, end=' ')