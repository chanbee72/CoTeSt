"""
두 큐 합 같게 만들기
"""
from collections import deque

def solution(queue1, queue2):
    queue1, queue2 = deque(queue1), deque(queue2)
    if (sum(queue1) + sum(queue2)) % 2 == 1:
        return -1
    
    cnt = 0
    target = (sum(queue1) + sum(queue2)) // 2

    if sum(queue1) == target:
        return 0
    
    sum_queue = sum(queue1)

    while sum_queue != target:
        if sum_queue < target:
            if queue2:
                element = queue2.popleft()
                queue1.append(element)
                sum_queue += element
            else:
                return -1
        else:
            element = queue1.popleft()
            sum_queue -= element

        cnt += 1

    return cnt