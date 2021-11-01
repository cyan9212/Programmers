def solution(n, computers):
    check = [False]*n
    nodes = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if computers[i][j] == 1:
                nodes[i].append(j)
    answer = 0
    def dfs(x):
        check[x] = True
        for y in nodes[x]:
            if check[y] == False:
                dfs(y)
                
    for i in range(n):
        if not check[i]:
            dfs(i)
            answer+=1
    return answer
