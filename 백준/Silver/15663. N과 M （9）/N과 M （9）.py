import sys
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
numbers = [i for i in map(int, input().rstrip().split())]
numbers.sort()

arr = []
visited = []
def dfs() :
    if len(arr) == M :
        print(*arr)
        return
    prevN = 0
    for i in range(N) :
        if i not in visited and prevN != numbers[i] :
            prevN = numbers[i]
            visited.append(i)
            arr.append(numbers[i])
            dfs()
            arr.pop()
            visited.pop()
dfs()