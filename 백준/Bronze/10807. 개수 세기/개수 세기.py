import sys
inputNumCount = int(sys.stdin.readline())
inputNumbers = list(map(int, sys.stdin.readline().split(' ')))
findNumber = int(sys.stdin.readline())
print(inputNumbers.count(findNumber))