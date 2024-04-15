'''
https://www.acmicpc.net/problem/17413
단어 뒤집기2
문자열을 자르긴 잘라야될거 같은데
'''
import sys
import re

input = sys.stdin.readline
originStr = input().rstrip()
splits = re.split(r'(<|>)', originStr)
isOpenBrace = False
_stack = []
for i in range(len(splits)) :
    #d열린 태그가 나왔다
    if splits[i] == '<' :
        isOpenBrace = True
    elif splits[i] =='>':
        isOpenBrace = False
    if isOpenBrace :
        _stack.append(splits[i])
    else :
        words = splits[i].split(' ')
        for j in range(len(words)) :
            _stack.append(words[j][::-1])
            if j < len(words) -1 :
                _stack.append(' ')



print(''.join(_stack))

# for c in originStr :
