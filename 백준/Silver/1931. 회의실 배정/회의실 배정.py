'''
https://www.acmicpc.net/problem/1931
회의실 배정
'''
import sys
input = sys.stdin.readline
N = int(input())
times = []
for _ in range(N) :
    s, e = map(int, input().rstrip().split())
    times.append((s, e))

#끝나는게 일찍 끝나야 여러개 할 수 있겠지? e를 기준으로 sort하고 e가 같으면 s로 정렬.
times.sort(key= lambda x : (x[1], x[0]))
#마지막 endTime 보다 시작 시간이 크거나 같으면 ++count 하면서 lastE 갱신.
lastE = 0
count = 0
for s, e in times :
    if lastE <= s :
        lastE = e
        count+=1
print(count)