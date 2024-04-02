#IPv6
import sys
shortAddr = sys.stdin.readline().rstrip().split(':')

resultAddr = ["0000" for _ in range(8)]
blankCount = shortAddr.count('')
addrCountDiff = 8 - len(shortAddr) + blankCount
if shortAddr.count('') > 0 :
    idx = shortAddr.index('')
    for i in range(addrCountDiff) :
        shortAddr.insert(idx, '0000')

shortAddr = [s for s in shortAddr if s]
for i in range(8) :
    resultAddr[i] = shortAddr[i].zfill(4)

print(':'.join(resultAddr))