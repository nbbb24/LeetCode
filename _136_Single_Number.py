class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        result=nums[0]
        for n in nums[1:]:
            result^=n
        return result

