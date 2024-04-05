'''
3. 좌표압축
작은 숫자 순으로 1씩 더하는거
원래 인덱스를 알아야하니 value, index 형태로 바꾸자.
'''
import sys
input = sys.stdin.readline
input()
numbers = [[x, i] for i,x in enumerate(map(int, input().rstrip().split()))]
numbers.sort()
n = 0
prevN = numbers[0][0]
for t in numbers :
    if t[0] != prevN :
        prevN = t[0]
        n += 1
    t[0] = n
numbers = [t[0] for t in sorted(numbers, key=lambda x:x[1])]
print(*numbers)
