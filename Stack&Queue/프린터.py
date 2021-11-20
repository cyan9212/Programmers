def solution(p, location):
    answer = 0
    check = [False]*len(p)
    check[location] = True
    while p:
        if p[0] == max(p):
            p.pop(0)
            if check.pop(0) == True:
                return answer+1
            else:
                answer+=1
        else:
            p.append(p.pop(0))
            check.append(check.pop(0))
