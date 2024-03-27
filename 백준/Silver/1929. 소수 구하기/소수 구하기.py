import sys
import math
M, N = map(int, sys.stdin.readline().replace('\n', '').split(' '))
def isPrimeNumber (num):
    if num == 1 :
        return True
    for i in range(2, int(math.sqrt(num)) +1) :
        if num % i == 0:
            return False
    return True

for i in range(M, N+1) :
    if i == 1 :
        continue
    if isPrimeNumber(i) :
        print(i)
