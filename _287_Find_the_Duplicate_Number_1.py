class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow=nums[nums[0]]
        fast=nums[nums[nums[0]]]
        while slow!=fast:
            slow=nums[slow]
            fast=nums[nums[fast]]
        
        slow=nums[0]
        while slow!=fast:
            slow=nums[slow]
            fast=nums[fast]
        
        return slow


# class Solution(object):
#     def findDuplicate(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         dicts={}
#         for n in nums:
#             if n not in dicts:
#                 dicts[n]=1
#             else:
#                 return n

