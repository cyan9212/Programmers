import heapq
def solution(scoville, K):
    heap = []
    answer = 0
    for x in scoville:
        heapq.heappush(heap,x)
    while len(heap)!=1:
        if heap[0]>K:
            return answer
        else:
            s1 = heapq.heappop(heap)
            s2 = heapq.heappop(heap)
            heapq.heappush(heap,s1+s2*2)
        answer+=1
    if heap[0]>K:
        return answer
    else:
        return -1
