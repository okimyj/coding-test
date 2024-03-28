import sys
input = sys.stdin.readline
employees = set()
for i in range(int(input())) :
    name, status = input().rstrip().split(' ')
    if status == 'enter' :
        employees.add(name)
    else :
        employees.remove(name)

for name in sorted(employees, reverse=True) :
    print(name)

