import itertools
def solution(str1, str2):
    answer = 0
    str1 = str1.upper()
    str2 = str2.upper()
    length1 = len(str1)
    length2 = len(str2)
    set1 = []
    set2 = []
    print(set(set1) & set(set2))
    for i in range(length1-1):
        temp = str1[i]+str1[i+1]
        if temp.isalpha():
            set1.append(temp)
    for i in range(length2-1):
        temp = str2[i]+str2[i+1]
        if temp.isalpha():
            set2.append(temp)
    if not set1 and not set2:
        return 65536
    u = list(itertools.chain(set1,set2))
    v = []
    for x in set1:
        if x in set2:
            index = set2.index(x)
            v.append(set2.pop(index))
    answer = int(len(v)/(len(u)-len(v))*65536)
    return answer
