import sys
input = sys.stdin.readline
subjectNum = int(input())
scores = list(map(int, input().rstrip().split(' ')))
maxScore = max(scores)
scores = list(map(lambda x:x/maxScore*100, scores))
print(sum(scores) / subjectNum)