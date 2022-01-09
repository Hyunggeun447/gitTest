# 다음 큰 숫자_프로그래머스 https://programmers.co.kr/learn/courses/30/lessons/12911

def solution(n):
    answer = 0
    b = format(n, 'b')
    # print(b)
    b_num = b.count('1')
    # print(b_num)
    
    for i in range(n+1,1_000_001):
        b=format(i, 'b')
        if b.count('1') == b_num:
            answer=i
            break
    
    
    
    return answer