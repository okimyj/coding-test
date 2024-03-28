import sys
str = sys.stdin.readline().rstrip().upper()
countDict = {}
for c in str :
    countDict[c] = (countDict.get(c) or 0)+1

sortedList = sorted(countDict.items(), key=lambda x:x[1], reverse=True)
if len(sortedList) > 1 and sortedList[0][1] == sortedList[1][1] :
    print('?')
else:
    print(sortedList[0][0])