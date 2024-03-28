import sys
input = sys.stdin.readline
input()
cardArr = input().rstrip().split(' ')
cardDict = {}
for card in cardArr :
    cardDict[card] = (cardDict.get(card) or 0) + 1
input()
checkCardArr = input().rstrip().split(' ')
for i, card in enumerate(checkCardArr) :
    if i == len(checkCardArr)-1 :
        print((cardDict.get(card) or 0), end='')
    else:
        print((cardDict.get(card) or 0), end=' ')