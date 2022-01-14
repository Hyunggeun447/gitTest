# 단어공부


import sys
input = sys.stdin.readline

word=str(input().strip())

dict={}

for i in word:
    if i.upper() not in dict:
        dict[i.upper()]=0
    dict[i.upper()]+=1

# print(dict)

count=0
ans=""
for key, value in dict.items():
    if value>count:
        count=value
        ans=key
    elif value == count:
        ans="?"
print(ans)