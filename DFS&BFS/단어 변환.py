from collections import deque
def solution(begin, target, words):
    if target not in words:
        return 0
    answer = 0
    words.append(begin)
    dic = {}
    dist = {i:float('inf') if i!=begin else 0 for i in words}
    length = len(words)
    word_size = len(words[0])
    for i in range(length):
        for j in range(length):
            if i == j:
                continue
            cnt = 0
            for k in range(word_size):
                if words[i][k] == words[j][k]:
                    cnt+=1
            if cnt == word_size-1:
                dic[words[i]] = dic.get(words[i],[]) + [words[j]]
    q = deque([begin])
    while q:
        cur = q.popleft()
        if cur == target:
            break
        for x in dic[cur]:
            q.append(x)
            if dist[x] > dist[cur]+1:
                dist[x] = dist[cur]+1
        dic[cur] = []
    if dist[target] == float('inf'):
        return 0
    return dist[target]
