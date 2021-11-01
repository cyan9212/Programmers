import heapq
def solution(operations):
    answer = []
    heap = []
    for x in operations:
        command,num = x.split()
        if command == 'D':
            if not heap:
                continue
            if num == '-1':
                heapq.heappop(heap)
            else:
                heap.pop()
        else:
            heapq.heappush(heap,int(num))
    if not heap:
        return [0,0]
    return [max(heap),min(heap)]
