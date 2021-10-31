import sys
sys.setrecursionlimit(100000)
ans = 8
def go(n,number,cur,cnt):
    if cur>number:
        return
    if cur == number:
        global ans
        if ans > cnt:
            ans = cnt
    go(n,number,cur+n,cnt+1)
    go(n,number,cur+1,cnt+2)
    go(n,number,cur+11,cnt+3)
    go(n,number,cur+111,cnt+4)
    go(n,number,cur+1111,cnt+5)
    go(n,number,cur+11111,cnt+6)
    
def solution(n, number):
    answer = go(n,number,0,0)
    return answer
