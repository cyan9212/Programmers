def solution(m, n, puddles):
    answer = 0
    mod = 1000000007
    d = [[0]*(m+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if i == 1 and j == 1:
                d[i][j] = 1
            else:
                temp = [j,i]
                if temp not in puddles:
                    d[i][j] = d[i-1][j] + d[i][j-1]
                    d[i][j]%=mod


    return d[n][m]%mod
