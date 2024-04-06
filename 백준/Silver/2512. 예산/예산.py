'''
https://www.acmicpc.net/problem/2512
예산
'''
import sys
input = sys.stdin.readline
N = int(input())
budgets = list(map(int, input().rstrip().split()))
maxBudget = int(input())
answer = 0
start = 1
end = maxBudget
if sum(budgets) <= maxBudget :
    print(max(budgets))
    exit(0)
while start <= end :
    mid = (start+end) // 2
    total = 0
    for budget in budgets :
        total += min(budget, mid)

    if total <= maxBudget :
        start = mid +1
        answer = mid
    else :
        end = mid -1
print(answer)