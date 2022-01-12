# 프로그래머스 단어변환

from collections import deque
import math
def solution(begin, target, words):
    answer = math.inf
    if target not in words:
        return 0
    
    dq=deque()
    check=[False for _ in range(len(words))]
    # print(check)
    dq.append([begin,0])
    
    while dq:
        [now,count] = dq.popleft()
        if now ==target:
            answer=min(answer,count)
            continue
        
        for i in range(len(words)):
            
            if check[i] == True:
                continue
            same=0
            
            for j in range(0,len(now)):
                if now[j] == words[i][j]:
                    same+=1
                    
            if same+1 == len(now):
                dq.append([words[i],count+1])
                check[i]=True
        
    
    
    return answer

print(solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit","cog",["hot", "dot", "dog", "lot", "log"]))