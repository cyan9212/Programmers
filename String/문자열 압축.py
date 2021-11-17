def solution(s):
    answer = 10000
    for n in range(1,len(s)//2+2):
        res = ''
        cnt = 1
        temp = s[:n]
        
        for i in range(n, len(s)+n, n):
            if temp == s[i:i+n]:
                cnt+=1
            else:
                if cnt==1:
                    res+=temp
                else:
                    res+=str(cnt)+temp
                temp = s[i:i+n]
                cnt=1
        answer = min(answer,len(res))
    return answer
