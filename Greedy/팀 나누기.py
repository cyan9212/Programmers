def solution(catalogue):
    lst = catalogue.split()
    N = lst[0]; K = lst[1]; D = lst[2]
    D = int(D)
    stack = []
    length = len(lst)
    for i in range(3,length,3):
        for j in range(int(lst[i]),int(lst[i+1])+1,int(lst[i+2])):
            stack.append(j)
    stack.sort()
    stack_length = len(stack)
    return stack[D%stack_length-1]
