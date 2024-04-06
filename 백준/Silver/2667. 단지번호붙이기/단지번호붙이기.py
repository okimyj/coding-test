'''
https://www.acmicpc.net/problem/2667
단지 번호 붙이기 : BFS, DFS
'''
import sys
input = sys.stdin.readline
N = int(input())
_map = [list(input().rstrip()) for _ in range(N)]
# print(_map)
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
areaList = []
def isInRange(r, c) :
    return r >= 0 and r < N and c >= 0 and c < N
def dfs(r, c) :

    for i in range(4):
        nextR = r + dr[i]
        nextC = c + dc[i]
        if isInRange(nextR, nextC) and _map[nextR][nextC] == '1' :
            areaList[len(areaList)-1]+=1
            _map[nextR][nextC] = '0'
            dfs(nextR, nextC)


for i in range(N) :
    for j in range(N):
        if _map[j][i] == '1' :
            _map[j][i] = '0'
            areaList.append(1)
            dfs(j, i)

areaList.sort()
print(len(areaList))
print(*areaList, sep='\n')

