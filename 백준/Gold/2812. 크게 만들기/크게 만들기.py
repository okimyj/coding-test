'''
https://www.acmicpc.net/problem/2812
크게 만들기
최대한 앞자리에 있으면서 작은 숫자를 지워야 가장 큰 수를 얻을 수 있다.
숫자 하나씩 stack 에 넣으면서 그 다음 숫자와 비교해 stack의 top에 있는 숫자가 작은 경우 pop 하는 것을 K개를 지울 때 까지 반복.
'''
import sys
input = sys.stdin.readline
N, K = map(int, input().rstrip().split())
number = input().rstrip()
cnt = 0
_stack = []
for n in number :

    while cnt < K and _stack and _stack[len(_stack)-1] < n :
        _stack.pop()
        cnt += 1
    _stack.append(n)

while cnt < K :
    _stack.pop()
    cnt+=1
print(''.join(_stack))




# print("cnt : " , cnt, "n : ", n)
#     if cnt < K and _stack and _stack[len(_stack)-1] > n :
#         cnt+=1
#     else :
#         _stack.append(n)