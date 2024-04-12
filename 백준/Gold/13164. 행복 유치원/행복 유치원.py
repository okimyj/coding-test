'''
https://www.acmicpc.net/problem/13164
행복 유치원
단체 티셔츠 비용 구하기.
K 개의 조는 같은 사이즈의 옷을 입고 비용은 가장 큰 키 - 가장 작은 키 만큼 듬.
모든 조원의 키가 같다 = 비용 0
인접한 원생들의 키 차이를 구하고 오름차순으로 정렬한 뒤 N-K 개를 제외한 합이 최소 비용.
인원수가 같을 필요는 없다

'''
import sys
input = sys.stdin.readline
N, K = map(int, input().rstrip().split())
heights = list(map(int, input().rstrip().split()))
heightsDiff = []
for i in range(len(heights)-1) :
    heightsDiff.append(heights[i+1] - heights[i])

heightsDiff.sort()

cost = sum(heightsDiff[:N-K])
print(cost)
