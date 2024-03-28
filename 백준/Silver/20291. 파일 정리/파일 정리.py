import sys
input = sys.stdin.readline
extensionDict = {}
for i in range(int(input())):
    name, extension = input().rstrip().split('.')
    extensionDict[extension] = (extensionDict.get(extension) or 0) +1

for data in sorted(extensionDict.items()) :
    print(str.format('{} {}', data[0], data[1]))