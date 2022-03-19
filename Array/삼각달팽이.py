from collections import deque
def solution(n):
    table = [[0]*n for _ in range(n)]
    length = n*(n+1)//2
    cnt=1
    cur = [0,0]
    direc = deque([[1,0], [0,1], [-1,-1]])
    
    while cnt!=length+1:
        x = cur[0]; y = cur[1];
        table[x][y] = cnt
        if x+direc[0][0]>=n or y+direc[0][1]>=n or table[x + direc[0][0]][y + direc[0][1]] !=0:
            temp = direc.popleft()
            direc.append(temp)
        
        cur[0]+=direc[0][0]
        cur[1]+=direc[0][1]
        cnt+=1
    answer = []
    for i in range(n):
        for j in range(n):
            if table[i][j]!=0:
                answer.append(table[i][j])
    return answer
