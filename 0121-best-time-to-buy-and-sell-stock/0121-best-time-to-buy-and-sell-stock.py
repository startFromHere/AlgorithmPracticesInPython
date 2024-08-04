class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        ans = 0
        for price in prices:
            if price - buy > ans:
                ans = price - buy
            elif price < buy:
                buy = price
        return ans
                

        