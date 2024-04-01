# https://www.acmicpc.net/problem/1018
# 체스판 다시 칠하기
import sys
from collections import deque
clipSize = 8
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
board = [list(input().rstrip()) for _ in range(N)]
rows = len(board)
cols = len(board[0])
visited = [[False for _ in range(M)] for _ in range(N)]
minCount = clipSize*clipSize
# 시작 지점 문자열만 생각하고 체크했더니 마지막 하나만 W인 경우 문제.. 
# count를 2개로 세자.
def check(r, c) :
  countW = 0 
  countB = 0
  for addR in range(clipSize) :
      for addC in range(clipSize) :
          
        if abs(addR - addC) % 2 == 0 :
          if 'W' != board[r+addR][c+addC] :
            countW += 1
          else :
            countB +=1
        elif abs(addR - addC) % 2 != 0 :
          if 'W' == board[r+addR][c+addC] :
            countW += 1
          else :
            countB +=1
        
  
  return min(countW, countB)
    

for r in range(rows-clipSize+1) :
  for c in range(cols-clipSize+1) :
    minCount = min(minCount, check(r, c))

print(minCount)