class Solution:
    def maxProfit(self, prices):
        minprice = float('inf')
        profit = 0 

        for price in prices:   
            minprice = min(minprice, price)
            profit = max(profit, price - minprice)

        return profit

