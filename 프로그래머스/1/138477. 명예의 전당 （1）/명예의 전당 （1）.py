from queue import PriorityQueue
def solution(k, score):
    # 우선순위 큐 사용 (우선순위가 높은(낮은 숫자)를 dequeue함.)
    q = PriorityQueue()
    answer = []
    for s in score :
        # 큐의 사이즈가 k 보다 크거나 같으면 가장 낮은 숫자를 dequeue하고 현재 s와 비교해서 큰 값을 s로 삼음.
        if q.qsize() >= k :
            s = max(s, q.get())
        # enqueue.
        q.put(s)
        # 가장 낮은 점수 append.
        answer.append(q.queue[0]);
    return answer