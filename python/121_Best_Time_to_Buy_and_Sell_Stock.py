class Solution(object):
    def maxProfit(self, prices):
        total = 0
        min_price = prices [0]
        for i in prices:
            if i < min_price:
                min_price = i
            elif i - min_price > total:
                total = i - min_price
        return total