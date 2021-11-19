def solution(genres, plays):
    answer = []
    dic = {}
    dic2 = {}
    rank = []
    length = len(plays)
    for i in range(length):
        dic[genres[i]] = dic.get(genres[i],0) + plays[i]
    for x in dic.keys():
        rank.append([dic[x],x])
    rank.sort(reverse=True)
    for x in rank:
        dic2[x[1]] = []
    for i in range(length):
        dic2[genres[i]] = dic2.get(genres[i]) + [(i,plays[i])]
    for x in dic2.keys():
        temp = dic2[x]
        temp.sort(key=lambda x:(x[1],-x[0]))
        for _ in range(2):
            if temp:
                answer.append(temp.pop()[0])
    return answer
