import sys
input = sys.stdin.readline
input()
numbers = map(int, input().rstrip().split())
nextN = 1
_stack = []

for n in numbers :
    if n != nextN :
        _stack.append(n)
    else :
        nextN = n+1
        while _stack and _stack[len(_stack)-1] == nextN :
            _stack.pop()
            nextN +=1

print(len(_stack) == 0 and 'Nice' or 'Sad')
