'''
stack - 쇠막대기
https://www.acmicpc.net/problem/10799
R (((RR)(R)R))(R)
'''
import sys
input = sys.stdin.readline
str = input().rstrip().replace('()', 'R')
_stack = []
count = 0
cutNum = 0
for c in str :
    if c == '(' :
        _stack.append(cutNum)
    elif c == 'R' :
        cutNum+=1
    elif c == ')' :
        count += cutNum - _stack.pop() + 1
print(count)



