import sys
input = sys.stdin.readline
A1, A0 = map(int, input().rstrip().split(' '))
C = int(input())
N = int(input())
print((A1 * N + A0 <= C * N and A1 <= C) and 1 or 0)