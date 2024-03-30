# 4일차 - 5번 팰린드롬 만들기
# I'm Sorry Hansoo
import sys
from collections import defaultdict
wtf = defaultdict(int)
for c in sys.stdin.readline().rstrip() :
    wtf[c] += 1
# dict sort
wtf =  sorted(wtf.items())
def make() :
    # 홀수인게 하나 이상이면 안 됨. 가운데 하나만 들어올 수 있으니까....
    oddChar = ''
    answer = ''
    for c in wtf :
        if c[1] % 2 != 0 :
            if oddChar != '' :
              return "I'm Sorry Hansoo"
            oddChar = c[0]
            if c[1] > 1 :
                answer += c[0] * (c[1] // 2)
        else :
            answer += c[0] * (c[1]//2)

    return(answer + oddChar + answer[::-1])

print(make())