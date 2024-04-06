'''
https://www.acmicpc.net/problem/1012
유기농배추
'''
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
def isInRange(r, c, _map) :
    return r >= 0 and r < len(_map) and c >= 0 and c < len(_map[0])
def dfs(r, c, _map) :
    for i in range(4) :
        nextR = r + dr[i]
        nextC = c + dc[i]
        if isInRange(nextR, nextC, _map) and _map[nextR][nextC] == 1 :
            _map[nextR][nextC] = 0
            dfs(nextR, nextC, _map)
def countAreaNum(_map) :
    count = 0
    for r in range(len(_map)) :
        for c in range(len(_map[0])) :
            if _map[r][c] == 1 :
                count +=1
                _map[r][c] = 0
                dfs(r, c, _map)
    return count

for _ in range(int(input())) :
    W, H, P = map(int, input().rstrip().split())
    _map = [[0] * W for _ in range(H)]
    for _ in range(P) :
        x, y = map(int, input().rstrip().split())
        _map[y][x] = 1
    print(countAreaNum(_map))