def solution(a):
    answer = 0
    length = len(a)
    d = [[0]*length for _ in range(length)]
    d[0][0] = a[0][0]
    for i in range(length):
        for j in range(i+1):
            if j == 0:
                d[i][j] = d[i-1][j]+a[i][j]
                continue
            if j == i:
                d[i][j] = d[i-1][j-1]+a[i][j]
                continue
            d[i][j] = max(d[i-1][j-1],d[i-1][j])+a[i][j]
    answer = max(d[length-1])
    return answer
