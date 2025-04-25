#Problem Statement:
'''You are given an array prices where prices[i] is the price of a stock on day i.
You want to maximize profit by choosing one day to buy and a future day to sell.
Return the maximum profit possible. If no profit exists, return 0.'''

#so the best day to sell would be the highest price and vice versa but we cant sell in the past so... yeah.  
prices = [7, 1, 5, 3, 6, 4]
# Buy at 1 (Day 2), sell at 6 (Day 5)
# Profit = 5 

def forex_trader(prices):
    if len(prices) < 2:  # Edge case: Not enough days to trade
        return 0
    
    min_price = float("inf")
    max_profit = 0
    
    for price in prices:
        if price < min_price:
            min_price = price 
            
        current_profit = price - min_price
        if current_profit > max_profit:
            max_profit = current_profit
    return max_profit
print(forex_trader(prices))