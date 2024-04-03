#문자열 폭발
import sys
input = sys.stdin.readline
a = input().rstrip()
b = input().rstrip()
bLen = len(b)
_stack = []
for c in a :
    _stack.append(c)
    if ''.join(_stack[-bLen::]) == b :
        for _ in range(bLen):
            _stack.pop()

joinStr = ''.join(_stack)

print(len(joinStr) <= 0 and 'FRULA' or joinStr)