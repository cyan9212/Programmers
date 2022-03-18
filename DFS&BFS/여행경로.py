from collections import deque
from collections import defaultdict

def solution(tickets):
    
    def init_graph():
        graph = defaultdict(list)
        for key, value in tickets:
            graph[key].append(value)
        return graph
    
    def dfs():
        q = deque(['ICN'])
        path = [] # 가려고 하는 경로를 저장
        while q:
            cur = q[-1]
            # 특정 공항에서 출발하는 표가 없거나 티켓을 다 써버린 경우
            if cur not in graph or len(graph[cur]) == 0:
                path.append(q.pop())
            else:
                q.append(graph[cur].pop())
        return path[::-1]
          
        
    graph = init_graph()
    for node in graph:
        graph[node].sort(reverse=True)
    
    answer = dfs()
    return answer
