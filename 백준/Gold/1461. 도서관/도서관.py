'''
https://www.acmicpc.net/problem/1461
도서관
책도 0, 나도 0에 있음.
책을 가져다놓고 다시 0에 왔다가 갔다가 해야됨.
한번에 M개를 들 수 있다.

우선 0을 기준으로 책 위치를 나눠놓고
양수는 내림차순 정렬, 음수는 오름차순 정렬함.
(M 개씩 돌았을 때 step수가 큰 녀석을 넣어야하니..) 

최소 걸음 수를 구하라. 너나구해!!!
'''
import sys
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
books = list(map(int, input().rstrip().split()))
positiveBooks = list(filter(lambda x : x > 0, books))
negativeBooks = list(filter(lambda x : x < 0, books))
positiveBooks.sort(reverse=True)
negativeBooks.sort()

moveSteps = 0
maxStep = 0
for i in range(0, len(positiveBooks), M) :
    maxStep = max(maxStep, abs(positiveBooks[i]))
    moveSteps += positiveBooks[i] *2
    
for i in range(0, len(negativeBooks), M):
    maxStep = max(maxStep, abs(negativeBooks[i]))
    moveSteps += abs(negativeBooks[i]) * 2


print(moveSteps - maxStep)