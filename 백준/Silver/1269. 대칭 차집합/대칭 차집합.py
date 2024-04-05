'''
1269 대칭 차집합
'''
import sys
input = sys.stdin.readline
input()
A = {x for x in input().rstrip().split()}
B = {x for x in input().rstrip().split()}
print(len(A-B) + len(B-A))