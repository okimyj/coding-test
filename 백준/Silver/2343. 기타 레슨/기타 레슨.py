'''
https://www.acmicpc.net/problem/2343
기타레슨
N : 강의 갯수
M : 블루레이 갯수
'''
import sys
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
lectures = list(map(int, input().rstrip().split()))
start = max(lectures)
end = 10000 * N
answer = 0
while start <= end :
    mid = (start + end) // 2
    count = 1
    acc = lectures[0]

    for i in range(1, len(lectures)) :
        if acc + lectures[i] > mid :
            count += 1
            acc = lectures[i]
        else :
            acc += lectures[i]

    # 만들어진 블루레이가 가지고 있는 블루레이의 갯수보다 크다.
    # 길이를 늘려준다.
    if M < count :
        start = mid +1
    else :
        answer = mid
        end = mid -1
print(answer)