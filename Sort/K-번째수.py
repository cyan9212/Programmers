def solution(array, commands):
    size = len(commands)
    answer = []
    for n in range(size):
        i = commands[n][0]-1
        j = commands[n][1]
        k = commands[n][2]-1
        temp = array[i:j]
        temp.sort()
        answer.append(temp[k])
    return answer
