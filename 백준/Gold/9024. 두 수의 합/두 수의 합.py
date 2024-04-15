'''
https://www.acmicpc.net/problem/9024
두 수의 합
K 에 가까운거니까 절대값으로 구해야한다.
'''
import sys
input = sys.stdin.readline


for _ in range(int(input())) :
    N, K = map(int, input().rstrip().split())
    numbers = list(map(int, input().rstrip().split()))
    numbers.sort()
    minDiff = sys.maxsize
    minCount = 0
    left = 0
    right = N-1
    while left < right :
        value = numbers[left] + numbers[right]
        if abs(K - value) < minDiff :
            minDiff = abs(K - value)
            minCount = 1
        elif abs(K - value) == minDiff :
            minCount+=1

        if value <= K :
            left +=1
        else :
            right -=1


    print(minCount)