'''
14425 문자열 집합
'''
import sys
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
S = {input().rstrip() for _ in range(N)}
count = 0
for _ in range(M) :
    i = input().rstrip()
    if i in S :
        count+=1
print(count)