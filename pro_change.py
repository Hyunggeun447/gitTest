# 프로그래머스 거스름돈

def solution(n, money):
    answer = 0
    
    dp=[1]+[0]*n
    
    for coin in money:
        for price in range(coin,n+1):
            if price >= coin:
                dp[price] += dp[price-coin]
            print(price,coin,dp)
                
    return dp[n]%1_000_000_007

print(solution(20,[1,2,5,7]))