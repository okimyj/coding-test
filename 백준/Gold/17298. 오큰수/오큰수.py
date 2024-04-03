# 오큰수
# 자신의 오른쪽에 있으면서 자기보다 큰 수 중 가장 왼쪽에 있는 수.
#
# 1,000,000개? 2중 for문은 x..
# 첫번째 값 부터 덱에 넣고, 덱의 0번째 값이 현재 넣으려는 값보다 작다면 현재 값을 출력 하고 popleft.
# 1. deque[3] cur = 3
# 2. deque[3] cur = 5 -> result[5], deque[5]
# 3. deque[5] cur = 2 -> result[5], deque[5, 2]
# 4. deque[5, 2] cur = 7 -> result[5, 7, 7] deque[7]

import sys
from collections import deque
input = sys.stdin.readline
input()
numbers = list(map(int, input().rstrip().split()))
result = [-1 for _ in range(len(numbers))]
reserve = deque()
for i, n in enumerate(numbers):
    while reserve :
        if reserve[0][0] < n :
            result[reserve[0][1]] = n
            reserve.popleft()
        else :
            break;
    reserve.appendleft((n, i))
print(*result)
# numbers 뒤집어서 뒤에서부터 넣는 방식.. 시간초과
# numbers.reverse()
# q = deque()
# result = deque()
# for n in numbers :
#     # 내가 q의 마지막 값 보다 크다 == 내가 오른쪽에 있는 숫자 중에 제일 크다. popleft.
#     if len(q) > 0 and  n > q[len(q)-1]:
#         q.pop()
#     # print("n : " , n , "q : " , q)
#     find = -1
#     for v in q :
#         if n < v :
#             find = v
#             break
#     result.appendleft(find)
#     q.appendleft(n)
#
# # result.reverse()
# print(*result)