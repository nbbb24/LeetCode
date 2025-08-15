class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left=1
        n=len(nums)
        right=n-1
        while left<right:
            mid=(left+right)//2
            count=sum([1 for n in nums if n<=mid])
            if count>mid:
                right=mid
            else:
                left=mid+1
        return left