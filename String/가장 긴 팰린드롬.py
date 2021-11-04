def solution(s):
    length = len(s)
    answer = len(s)
    flag  = 0
    while answer!=0:
        for i in range(length-answer+1):
            temp = s[i:answer+i]
            if temp == temp[::-1]:
                flag = 1
                break
        if flag == 1:
            break
        answer-=1
    return answer
