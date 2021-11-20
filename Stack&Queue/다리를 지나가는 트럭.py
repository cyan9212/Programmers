from collections import deque
def solution(bridge_length, weight, truck_weights):
    time = 0
    q = deque([0]*(bridge_length))
    truck_weights = deque(truck_weights)
    summ = 0
    while q:
        time+=1
        summ-=q.popleft()
        if truck_weights:
            if summ+truck_weights[0]<=weight:
                summ+=truck_weights[0]
                q.append(truck_weights.popleft())
                
            else:
                q.append(0)
    return time
