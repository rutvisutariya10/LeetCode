class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l, r = 0, 0
        while r < len(prices):
        maxProfit = 0
            if prices[r] < prices[l]:
                l = r
            curr = prices[r] - prices[l]
            maxProfit = max(maxProfit,curr)
            r += 1
        return maxProfit
