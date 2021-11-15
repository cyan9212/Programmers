from itertools import product
from itertools import chain
def solution(word):
    alpha = 'AEIOU'
    dic = []
    for i in range(1,6):
        dic.extend(product(alpha,repeat=i))
    dic.sort()
    for i,d in enumerate(dic):
        temp = ''
        for w in d:
            temp+=w
        if temp == word:
            return i+1
