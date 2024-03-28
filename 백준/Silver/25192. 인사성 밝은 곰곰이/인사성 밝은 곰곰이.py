import sys
input = sys.stdin.readline
useEmoji = set()
count = 0
for i in range(int(input())) :
    line = input().replace('\n', '')
    if line == "ENTER" :
        useEmoji.clear()
    elif line not in useEmoji :
        count += 1
        useEmoji.add(line)

print(count)