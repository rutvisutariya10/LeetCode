class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit = 0
        currProf = 0
        left = 0
        right = 0
        while right < len(prices):
            if prices[right] < prices[left]:
                left = right
            else:
                currProf = prices[right] - prices[left]
                if currProf > maxProfit:
                    maxProfit = currProf
            right += 1
        return maxProfit
            