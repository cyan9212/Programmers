import heapq
def solution(n, works):
    answer = 0
    length = len(works)
    for i in range(length):
        works[i] = works[i]*(-1)
    heapq.heapify(works)
    for _ in range(n):
        temp = heapq.heappop(works)
        if temp < -1:
            heapq.heappush(works,temp+1)
        else:
            heapq.heappush(works,0)
    for x in works:
        answer+=x*x
    return answer
