class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        maxpro=0
        start=prices[0]
        n=len(prices)
        for num in prices:
            maxpro=max(maxpro,num-start)
            if num < start:
                start=num
        return maxpro