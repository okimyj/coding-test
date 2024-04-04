'''
세 수의 합
[접근]
1. 서로 다른 인덱스 조합인 줄 알았는데 잘 읽어보니 세 수와 결과수까지 서로 같은 수여도 상관없음. (0+0+0=0)
2. 가능한 두 수의 합을 먼저 구해놓고, target - x = 두 수의 합 이 되는 수를 구해보자.
'''
import sys
from collections import defaultdict
input = sys.stdin.readline
numbers = []
twoSumList = set()
numbersLen = int(input())
for _ in range(numbersLen) :
    numbers.append(int(input()))

for i in numbers :
    for j in numbers :
        twoSumList.add(i+j)

numbers.sort()

for i in range(len(numbers)-1, -1, -1) :
    for j in range(i+1) :
        if numbers[i] - numbers[j] in twoSumList :
            print(numbers[i])
            exit()
        # x = numbers[i] - s
        # midIndex = bisect_right(numbers, x) - bisect_left(numbers, x)
        # if midIndex > 0 and x == numbers[midIndex] :
        #     print(numbers[i])
        #     exit()


