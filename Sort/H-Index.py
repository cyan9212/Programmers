def solution(n):
    answer = 0
    length = len(n)
    for i in range(1,length+1):
        cnt = 0
        for num in n:
            if num>=i:
                cnt+=1
        if cnt >= i:
            answer=i
    return answer
