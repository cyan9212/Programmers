import itertools
def prime(n):
    if n == 1 or n == 0:
        return False
    if n == 2:
        return True
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True

def solution(numbers):
    answer = 0
    length = len(numbers)
    stack = []
    for i in range(1,length+1):
        a = list(itertools.permutations(numbers,i))
        a = list(set(a))
        stack+=a
        
    check_list = []   
    for x in stack:
        temp = ''.join(x)
        check_list.append(int(temp))
    check_list = list(set(check_list))
    for x in check_list:
        if prime(x) == True:
            answer+=1
    return answer
