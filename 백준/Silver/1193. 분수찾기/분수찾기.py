import sys
x = int(sys.stdin.readline())
line = 1
diff = x
# 대각선으로 어느 라인에 있는지 찾자.
while line < diff :
    diff -= line
    line += 1

# 짝수 라인인 경우
if line % 2 == 0 :
    print("%d/%d" % (diff, line-diff+1))
else:
    print("%d/%d" % (line-diff+1, diff))