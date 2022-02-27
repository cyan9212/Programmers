def solution(new_id):
    new_id = new_id.lower() #1단계
    length = len(new_id)
    
    answer = '' #2단계
    for word in new_id:
        if word.isalnum() or word in '-_.':
            answer += word
    
    while '..' in answer: #3단계
        answer = answer.replace('..','.')
    
    answer = answer[1:] if answer[0] == '.' and len(answer) > 1 else answer #4단계
    answer = answer[:-1] if answer[-1] == '.' else answer
     
    if answer == '': #5단계
        answer = 'a'
    
    if len(answer)>=16: #6단계
        answer = answer[:15]
    if answer[-1] == '.':
        answer = answer[:-1]
    
    while len(answer)<=2: #7단계
        answer = answer+answer[-1]
        
    return answer 
