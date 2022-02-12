# 날짜 계산
import sys
input = sys.stdin.readline

e, s, m = map(int,input().split())

e_2, s_2, m_2 = 0,0,0

count=0

while True:
    e_2+=1
    s_2+=1
    m_2+=1
    count+=1
    if e_2 == 16:
        e_2=1
    if s_2 == 29:
        s_2=1
    if m_2 ==20:
        m_2=1
    if e_2 == e and s_2 == s and m_2 == m:
        print(count)
        break