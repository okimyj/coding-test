import sys
input = sys.stdin.readline
cardDict = {}
needBellCard = ""
for i in range(int(input())) :
    name, num = input().rstrip().split(' ')
    cardDict[name] = (cardDict.get(name) or 0) + int(num)

result = list(filter(lambda x:x[1] == 5, cardDict.items()))

print(len(result) > 0 and "YES" or "NO")