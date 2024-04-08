'''
https://www.acmicpc.net/problem/2467
용액
... 두 용액에서 정렬되었고 안되었고만 다른거 같은데?
'''
import sys
input = sys.stdin.readline
input()
numbers = list(map(int, input().rstrip().split()))
start = 0
end = len(numbers)-1
minV = sys.maxsize
selected = [0, 0]
while start < end :
    calc = numbers[start] + numbers[end]
    if abs(calc) < minV :
        selected[0] = numbers[start]
        selected[1] = numbers[end]
        minV = abs(calc)
        if calc == 0 :
            break
    if calc < 0 :
        start +=1
    else :
        end -= 1

print(*selected)