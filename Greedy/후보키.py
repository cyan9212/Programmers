def solution(relation):
    row = len(relation)
    col = len(relation[0])
    
    comb = []
    for i in range(1,col+1):
        comb.extend(combinations(range(col), i))
    
    unique = []
    for c in comb:
        temp = [tuple(item[key] for key in c) for item in relation]
        if len(set(temp)) == row:
            put = True
            
            for x in unique:
                if set(x).issubset(set(c)):
                    put = False
                    break
            if put: unique.append(c)
                
    return len(unique)
