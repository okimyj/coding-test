def solution(s, n):
    answer = ''
    def toCode(char, n) :
        if char == ' ':
            return ord(char)
        code = ord(char) + n
        if char.islower() :
            code = (code-ord('a')) % 26 + ord('a')
        else :
            code = (code-ord('A')) % 26 + ord('A')

        return code
    for char in s :
        answer += chr(toCode(char, n));
    return answer