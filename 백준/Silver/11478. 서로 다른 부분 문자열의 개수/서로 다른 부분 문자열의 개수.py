import sys
strArr = sys.stdin.readline().rstrip()
wordParts = set()
for i in range(len(strArr)) :
    parts = strArr[i]
    wordParts.add(parts)
    for j in range(i+1, len(strArr)) :
        parts += strArr[j]
        wordParts.add(parts)
print(len(wordParts))