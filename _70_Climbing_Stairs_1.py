class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=2:
            return n
        prev1=2
        prev2=1
        
        for i in range(3,n+1):
            cur=prev1+prev2
            prev2=prev1
            prev1=cur
        return prev1
