def solution(cards1, cards2, goal):
    while len(goal) :
        if len(cards1) > 0 and cards1[0] == goal[0] :
            cards1.pop(0)
        elif len(cards2) > 0 and cards2[0] == goal[0]:
            cards2.pop(0)
        else :
            break
        goal.pop(0)
        
    return len(goal) > 0 and "No" or "Yes"