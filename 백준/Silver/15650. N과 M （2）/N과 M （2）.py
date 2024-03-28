import sys
N, M = map(int, sys.stdin.readline().rstrip().split(' '))
arr =[]
def dfs(start) :
    if len(arr) == M :
        print(' '.join(map(str, arr)))
        return
    for i in range(start, N+1) :
        if i not in arr :
            arr.append(i)
            dfs(i+1)
            arr.pop()
dfs(1)