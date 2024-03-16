def solution(s):
    splitNums = list(map(int, s.split(' ')))
    return str.format('{} {}', min(splitNums), max(splitNums))
