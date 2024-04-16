'''
https://www.acmicpc.net/problem/2212
센서
'''
import sys
input = sys.stdin.readline
N = int(input())
K = int(input())
positions = list(map(int, input().rstrip().split()))
positions.sort()
posDiff = []
for i in range(len(positions)-1) :
    posDiff.append(positions[i+1]-positions[i])

posDiff.sort()

sum = 0
for i in range(N-K) :
   if posDiff[i] > 0 :
       sum += posDiff[i]
print(sum)