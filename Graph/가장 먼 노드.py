from collections import deque
            
def solution(n, edge):
    answer = 0
    visited = [-1]*(n+1)
    a = [[] for _ in range(n+1)]
    for i in edge:
        u,v = i[0],i[1]
        a[u].append(v)
        a[v].append(u)
    q = deque()
    q.append([1,0])
    while q:
        value = q.popleft()
        v = value[0]
        count = value[1]
        if visited[v] == -1:
            visited[v] = count
            count+=1
            for e in a[v]:
                q.append([e,count])
    for x in visited:
        if x == max(visited):
            answer+=1
    return answer
