def solution(s, n):
    def toCode(char) :
        if char == ' ':
            return ord(char)
        code = ord(char) + n
        if char.islower() :
            code = (code-ord('a')) % 26 + ord('a')
        else :
            code = (code-ord('A')) % 26 + ord('A')
        return code
    answer = ''
    
    for char in s :
        answer += chr(toCode(char));
    return answer