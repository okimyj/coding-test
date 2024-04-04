'''
오등 큰수
input array
[1, 1, 2, 3, 4, 2, 1]
count array
[1, 2, 1, 1, 1, 2, 3]

'''
import sys
from collections import defaultdict, deque
input = sys.stdin.readline
input()
numbers = list(map(int, input().rstrip().split()))
result = [-1 for _ in range(len(numbers))]
countDict = defaultdict(int)

for n in numbers :
    countDict[n] += 1

checkStack = []
for i in range(len(numbers)) :

    while checkStack :
        topIdx = checkStack[len(checkStack)-1]
        n = numbers[topIdx]
        curN = numbers[i]
        # checkStack 의 마지막에 있는 녀석의 갯수가 현재 i번째 녀석의 갯수 보다 큰지 체크.
        if countDict[n] < countDict[curN] :
            result[topIdx] = curN
            checkStack.pop()
        else :
            break
    checkStack.append(i)

# 시간초과
# for i in range(len(numbers)) :
#     obn = -1
#     for j in range(i, len(numbers)) :
#         if countDict[numbers[i]] < countDict[numbers[j]] :
#             obn = numbers[j]
#             break
#     result.append(obn)

print(*result)
