# 4일차 - 3번 끝말잇기
import sys
input = sys.stdin.readline
words = [input().rstrip() for i in range(int(input()))]
temp = [input().rstrip() for i in range(int(input()))]
temp = [x for x in temp if x not in words]
unknownIdx = words.index('?')
prevChar = unknownIdx > 0 and words[unknownIdx-1][-1:] or None
nextChar = unknownIdx < len(words)-1 and words[unknownIdx+1][0:1] or None

for word in temp :
    if (not prevChar or word[0:1] == prevChar) and (not nextChar or word[-1:] == nextChar) :
        print(word)
        break
