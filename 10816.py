# 숫자카드 2

import sys
input = sys.stdin.readline

n = int(input())
lst_num = list(map(int, input().split()))
m= int(input())
lst_cards = list(map(int, input().split()))

dict={}
for card in lst_cards:
    dict[card]=0

for num in lst_num:
    try:
        dict[num]+=1
    except:
        continue

# print(dict)
ans=[]
for card in lst_cards:
    ans.append(dict[card])

print(' '.join(map(str,ans)))
