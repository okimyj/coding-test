# 치킨 배달
import sys
import itertools
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
_map = [input().rstrip().split(' ') for _ in range(N)]
houseList = []
storeList = []
# 우선 각 집과 치킨집의 좌표를...
for r in range(len(_map)) :
    for c in range(len(_map[0])) :
        if _map[r][c] == '1' :
            houseList.append((r, c))
        elif _map[r][c] == '2':
            storeList.append((r, c))

dists = []
def calcDist(storeComb) :
    # 도시의 치킨 거리는 모든 집의 치킨거리의 합.
    # storeComb에서 각 집의 치킨거리 최소 값
    sumDist = 0
    for h in houseList :
        minDist = 9999999
        for s in storeComb :
            minDist = min(minDist, abs(s[0]-h[0]) + abs(s[1]-h[1]))
        sumDist+=minDist
    return sumDist

# store 중 M 개의 조합 생성.
for storeComb in itertools.combinations(storeList, M) :
    dists.append(calcDist(storeComb))


print(min(dists))

