# AC
# R - 배열에 있는 수의 순서를 뒤집음 [1, 2, 3, 4] -> [4, 3, 2, 1]
# D - 배열의 첫번째 인덱스를 버림
# 그냥 리스트 reverse, pop(0) 사용했더니 시간초과.
# deque 사용 시도.
import sys
from collections import deque
input = sys.stdin.readline

def D(q, isPopLeft):
    if len(q) <= 0 :
        return False
    if isPopLeft :
        q.popleft()
    else :
        q.pop()
    return True

# 첫 번째 입력 테스트 케이스 만큼 반복.
for i in range(int(input())) :
    operations = list(input().rstrip())
    # 입력 값 개수
    input()
    # 양옆 대괄호 자르기.
    strNumbers = input().rstrip()[1:-1]
    # strNumbers 길이가 0 보다 크면 split, 아니면 빈 배열로 덱 생성.
    numbers = deque(len(strNumbers) > 0 and list(map(int, strNumbers.split(','))) or [])
    isPass = False
    isPopLeft = True
    for op in operations :
        if op == 'R' :
            isPopLeft = not isPopLeft
            isPass = True
        elif op == 'D' :
            isPass = D(numbers, isPopLeft)
        if not isPass :
            break

    if isPass :
        if not isPopLeft :
            numbers.reverse()
        print('[{}]'.format(','.join(str(v) for v in numbers)))
    else:
        print('error')