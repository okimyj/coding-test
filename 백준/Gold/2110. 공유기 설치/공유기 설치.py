'''
2110 공유기 설치
1 2 4 8 9
1, 4, 8 // 1, 4, 9 에 설치하는데 왜 가장 인접한 공유기 거리가 둘 다 3임?...
아 ㅇㅋ 인접한 공유기 거리 중 최대 값... 그럼 막상 집 좌표는 상관이 없는건가? 도 아니고
설명 예쁘게 잘 써놨네.
-> 위에 다 아니고 그냥 설치할 수 있는 기준 거리 최대 값을 구하는 것...ㅋ
'''
import sys
input = sys.stdin.readline
N, C = map(int, input().rstrip().split())
houses = [int(input()) for _ in range(int(N))]
houses.sort()
start = 0
end = houses[N-1]
maxDist = 0
while start <= end :
    mid = (start + end) // 2
    count = 1
    lastDeploy = houses[0]
    
    for i in range(1, N) :
        if mid <= houses[i] - lastDeploy :
            count += 1
            lastDeploy = houses[i]

    # 배치해야되는 개수 이상 배치했음.
    if C <= count :
        # 배치 거리를 늘려줌.
        maxDist = mid
        start = mid+1
    else :
        # 배치 다 못함. 배치거리 좁힘.
        end = mid-1


print(maxDist)