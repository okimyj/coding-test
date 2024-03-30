import sys
from collections import defaultdict
input = sys.stdin.readline
N = int(input())
M = int(input())
S = input().rstrip()
# pattern = 'IO' * (N+1)
# pattern = pattern[:-1]
# print(pattern)
cNum = defaultdict(int)
count = 0
for i, c in enumerate(S) :
    # 연속으로 같은 문자열이 들어온 경우.
    if i > 0 and c == S[i-1] :
        cNum['I'] = c == 'I' and 1 or 0
        cNum['O'] = 0
        # print("i : ", i, " c : ", c, "cNum : ", cNum)
        continue

    if c == 'I' :
        cNum['I'] += 1
        if cNum['I'] == N+1 and cNum['O'] == N :
            count +=1
            cNum['I'] -= 1
            cNum['O'] -= 1
    elif cNum['I'] > 0 and c == 'O' :
        cNum['O'] += 1
    # print("i : ", i, " c : ", c, " cNum : ", cNum, " // count : " , count)
print(count)