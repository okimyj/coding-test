def solution(id_list, report, k):
    users = {key:{'receives':set(), 'request':set()} for key in id_list}
    for r in report :
        reporter, target = r.split(' ')
        users[reporter]['request'].add(target)
        users[target]['receives'].add(reporter)
    
    answer = [0 for i in range(len(id_list))]
    for i, id in enumerate(id_list) :
        for target in users[id]['request'] :
            if len(users[target]['receives']) >= k :
                answer[i]+=1
    
    return answer