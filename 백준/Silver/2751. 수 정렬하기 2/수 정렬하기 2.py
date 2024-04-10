'''
https://www.acmicpc.net/problem/2751
sort - 수 정렬하기 2
'''
import sys
input = sys.stdin.readline
N = int(input())
numbers = [int(input()) for _ in range(N)]
numbers.sort()
print(*numbers, sep='\n')