import sys
input = sys.stdin.readline
roomSize = int(input())
room = [list(input().rstrip()) for _ in range(roomSize)]

countR = 0
countC = 0
for r in range(roomSize) :
  rLength = 0
  cLength = 0
  
  for c in range(roomSize) :
    if room[r][c] == '.' :
      cLength +=1
    if room[r][c] == 'X' :
      if cLength >= 2 :
        countC +=1
      cLength = 0

    if room[c][r] == '.' :
      rLength += 1
    if room[c][r] == 'X' :
      if rLength >= 2 :
        countR +=1
      rLength = 0

  if cLength >= 2 :
    countC +=1
  if rLength >= 2 :
    countR += 1


print(countC, countR)


    