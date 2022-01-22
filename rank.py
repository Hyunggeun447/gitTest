# 프로그래머스 그래프 순위 lv3
from collections import deque
def solution(n, results):
    answer = 0
    los={}
    win={}
    for i in range(1,n+1):
        los[i]=[]
        win[i]=[]

    for i,j in results:
        if j not in los:
            los[j]=[]
        if i not in win:
            win[i]=[]
        
        los[j].append(i)
        win[i].append(j)
    
    print(los)
    print(win)
    
    
    def dfs(a,dict):
        tem=deque()
        tem.append(a)
        check=[False]*(n+1)
        check[a]=True
        count=0
        while tem:
            k=tem.popleft()
            for i in dict[k]:
                if check[i] == True:
                    continue
                else:
                    tem.append(i)
                    count+=1
                    check[i] = True
        return count
                
    for i in range(1,n+1):
        if dfs(i,win)+dfs(i,los) == n-1:
            answer+=1
    
    return answer


print(solution(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
