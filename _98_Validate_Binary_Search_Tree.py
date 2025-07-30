# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return True

        maxx=float('inf')
        minn=float('-inf')  
        return self.helper(root,minn,maxx) 
        

    def helper(self,root,minn,maxx):
        if not root:
            return True
        if root.val<=minn or root.val>=maxx:
            return False
        return self.helper(root.left,minn,root.val) and self.helper(root.right,root.val,maxx)
        
        