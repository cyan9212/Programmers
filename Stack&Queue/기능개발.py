from collections import deque
def solution(progresses, speeds):
    answer = []
    prog = deque(progresses)
    spee = deque(speeds)
    while prog:
        length = len(prog)
        for i in range(length):
            prog[i]+=spee[i]
        if prog[0]<100:
            continue
        else:
            cnt = 1
            prog.popleft()
            spee.popleft()
            while prog and prog[0]>=100:
                prog.popleft()
                spee.popleft()
                cnt+=1
            answer.append(cnt)
    return answer
