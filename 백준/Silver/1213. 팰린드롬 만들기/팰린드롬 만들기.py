import sys
from collections import defaultdict
wtf = defaultdict(int)
for c in sys.stdin.readline().rstrip() :
    wtf[c] += 1
# dict sort
# wtf =  sorted(wtf.items(), key = lambda x : (-x[1], x[0]))
wtf =  sorted(wtf.items())
def make() :
    # 홀수인게 하나 이상이면 안 됨.
    # 가운데 하나만 들어올 수 있으니까.... 무조건 알파벳 순으로 정렬해도 안되네?
    oddChar = ''
    answer = ""
    for c in wtf :
        if c[1] % 2 != 0 :
            if oddChar != '' :
              print("I'm Sorry Hansoo")
              return
            oddChar = c[0]
            if c[1] > 1 :
                answer += c[0] * (c[1] // 2)
        else :
            answer += c[0] * (c[1]//2)

    answer = answer + oddChar + answer[::-1]

    print(answer)

make()