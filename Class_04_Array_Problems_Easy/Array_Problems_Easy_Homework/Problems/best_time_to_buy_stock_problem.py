# Say you have an array for which the ith element is the price of a given stock on day i
# If you were only permitted to complete at most one transaction (i.e, buy one and 
# sell one share of the stock) design an algorithm to find the maximum profit
# This problem came from leetcode.com

input_array = [7, 1, 5, 3, 6, 4]
# Output = 5

#not optimized
def optimize_profit (array_prices) :
    profit = 0
    for buy_price in array_prices :
        for sell_price in array_prices :
            if sell_price - buy_price > profit :
                profit = sell_price - buy_price

    return profit

#optimized
def optimize_profit_optimized (array_prices):
    max = array_prices[0]
    min = array_prices[0]
    for price in array_prices :
        if price > max : max = price
        if price < min : min = price

    return max - min

