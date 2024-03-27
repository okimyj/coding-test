import sys
num = int(sys.stdin.readline())
lines = []
for i in range(6) :
    lines.append(list(map(int, sys.stdin.readline().split(' '))))
lines = lines * 2
for i in range(1, 12):
    if lines[i][0] == lines[i+2][0] and lines[i+1][0] == lines[i+3][0] :
        totalArea = lines[i-1][1] * lines[i+4][1]
        smallArea = lines[i+1][1] * lines[i+2][1]
        break

print(num * (totalArea - smallArea))