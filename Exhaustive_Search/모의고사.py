def solution(answers):
    answer = []
    s1 = [1,2,3,4,5]
    s2 = [2,1,2,3,2,4,2,5]
    s3 = [3,3,1,1,2,2,4,4,5,5]
    c = [0]*3
    index = 0
    for x in answers:
        if x == s1[index%5]:
            c[0]+=1
        if x == s2[index%8]:
            c[1]+=1
        if x == s3[index%10]:
            c[2]+=1
        index+=1
    for i in range(3):
        if c[i] == max(c):
            answer.append(i+1)
            
    return answer
