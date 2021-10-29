def solution(gems):
    num = len(set(gems))
    length = len(gems)
    dic = {gems[0]:1}
    left,right = 0,0
    answer = [0,length-1]
    while right<length:
        if len(dic) == num:
            if right - left < answer[1] - answer[0]:
                answer = [left,right]
            if dic[gems[left]] == 1:
                del dic[gems[left]]
            else:
                dic[gems[left]]-=1
            left+=1
        else:
            right+=1
            if right == length:
                break
            if dic.get(gems[right])is None:
                dic[gems[right]] = 1
            else:
                dic[gems[right]]+=1
            
    return [answer[0]+1,answer[1]+1]
