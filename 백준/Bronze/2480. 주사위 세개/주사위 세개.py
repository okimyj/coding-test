import sys
diceList = list(map(int, sys.stdin.readline().replace('\n', '').split(' ')))
dice = {}
for x in diceList :
    dice[x] = (dice.get(x) or 0) +1

dice = sorted(dice.items(), key=lambda x:x[1], reverse=True)
if len(dice) == 1 :
    print(10000 + dice[0][0] * 1000)
elif len(dice) == 2 :
    print(1000 + dice[0][0] * 100)
else :
    print(100 * max(diceList))
