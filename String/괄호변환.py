def divide(s):
    balance = 0
    u = ''
    v = ''
    for i,x in enumerate(s):
        if x == '(':
            balance+=1
        else:
            balance-=1
        if balance == 0:
            u = s[0:i+1]
            v = s[i+1:]
            break
    return u,v

def check(s):
    stack = [s[0]]
    s = s[1:]
    for x in s:
        if stack[-1] == '(' and x == ')':
            stack.pop()
        else:
            stack.append(x)
    if stack:
        return False
    else:
        return True 
def convert(s):
    result = ''
    for i in s:
        if i == '(':
            result+=')'
        else:
            result+='('
    return result

def solution(s):
    answer = ''
    while s:
        u,s = divide(s)
        if check(u):
            answer+=u
        else:
            answer+='('+solution(s)+')' + convert(u[1:-1])
            break
    return answer
