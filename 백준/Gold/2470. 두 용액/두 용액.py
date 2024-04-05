'''
두 용액
'''
import sys
input = sys.stdin.readline
itemNum = int(input())
items = list(map(int, input().rstrip().split()))
items.sort()
minV = sys.maxsize
selected = [0, 0]
start = 0
end = itemNum-1
while start < end :
    calc = items[start] + items[end]
    if abs(calc) < minV :
        minV = abs(calc)
        selected[0] = items[start]
        selected[1] = items[end]
        if calc == 0 :
            break

    if calc < 0 :
        start +=1
    else :
        end -=1

print(*selected)