def solution(brown, yellow):    
    for i in range(1,yellow+1):
        if yellow % i == 0:
            if (i+2)*((yellow//i)+2) == brown+yellow:
                if i>(yellow//i):
                    return [i+2,yellow//i+2]
                else:
                    return [yellow//i+2,i+2]
