import sys
n = int(sys.stdin.readline())
result = ""
for i in range(1, n*2) :
    if result != "" :
        result += "\n"
    startNum = i < n and i % n or n - i % n
    line = ('*' * startNum) + (' ' * (n-startNum))
    result += line + line[::-1]
    
print(result)