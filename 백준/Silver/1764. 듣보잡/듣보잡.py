# 4일차 - 4번 듣보잡
# 단순 배열 find 시간초과.
import sys
input = sys.stdin.readline
aNum, bNum = map(int, input().rstrip().split())
a = {input().rstrip() for x in range(aNum)}
b = {input().rstrip() for x in range(bNum)}
# a = [input().rstrip() for x in range(aNum)]
# b = [input().rstrip() for x in range(bNum)]
c = [x for x in a if x in b]
c.sort()

print(len(c))
print(*c, sep="\n")   # 개꿀...