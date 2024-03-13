def solution(sizes):
    max_w = 0
    max_h = 0
    for size in sizes :
        if size[0] < size[1] :
            temp = size[1]
            size[1] = size[0]
            size[0] = temp
        max_w = max(max_w, size[0])
        max_h = max(max_h, size[1])
    return max_w*max_h