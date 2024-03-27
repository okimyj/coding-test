import sys
testNum = int(sys.stdin.readline())
resultArr = []
for i in range(testNum) :
    repeat, str = sys.stdin.readline().replace('\n','').split(' ')
    repeat = int(repeat)
    result = ""
    for c in str :
        result += c * repeat
    resultArr.append(result)

for result in resultArr :
    print(result)