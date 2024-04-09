import sys
input = sys.stdin.readline
_stack = []
for _ in range(int(input())) :
    op = input().rstrip().split()
    if op[0] == 'push' :
        _stack.append(int(op[1]))
    elif op[0] == 'pop' :
        print(len(_stack) == 0 and -1 or _stack.pop())
    elif op[0] == 'size' :
        print(len(_stack))
    elif op[0] == 'empty' :
        print(len(_stack) == 0 and 1 or 0)
    elif op[0] == 'top':
        print(len(_stack) == 0 and -1 or _stack[-1])