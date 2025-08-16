class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums)<=1:
            return 
        left=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[left],nums[i]=nums[i],nums[left]
                left+=1

        