"""
Program to solve the best time to buy and sell stock given
the following conditions:

You are given an array prices where prices[i] is the price of a 
given stock on the ith day.

You want to maximize your profit by choosing a single day to buy 
one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you 
cannot achieve any profit, return 0.
"""
def maxProfit(prices):
    left_index, right_index, max_profit = 0, 1, 0 # left_index = buy, right_index = sell
    while right_index < len(prices):
        # profitable?
        if prices[left_index] < prices[right_index]:
            profit = prices[right_index] - prices[left_index]
            max_profit = max(max_profit, profit)
        else:
            left_index = right_index
        right_index += 1
    return max_profit

if __name__ == '__main__':
    print(maxProfit([7,1,5,3,6,4]))
    print(maxProfit([7,6,4,3,1]))