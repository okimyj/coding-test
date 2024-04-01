import sys
input = sys.stdin.readline
input()
A = list(map(int, input().rstrip().split()))
input()
M = list(map(int, input().rstrip().split()))

A.sort()

def binarySearch(target) :
  start=0
  end = len(A)-1
  while start <= end :
    mid = (start+end) // 2
    if A[mid] == target :
      print(1)
      return
    if A[mid] < target :
      start = mid+1
    else :
      end = mid -1
  print(0)

for target in M :
  binarySearch(target)