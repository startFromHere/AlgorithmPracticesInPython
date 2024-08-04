class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        ans = 0
        for p in prices:
            if p > buy:
                ans += p - buy
            buy = p
        return ans