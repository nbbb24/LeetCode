# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return True

        return self.helper(root.left,root.right)


    def helper(self,l,r):
        if not l and not r:
            return True
        elif l is None or r is None or l.val!=r.val:
            return False
        return self.helper(l.left,r.right) and self.helper(l.right,r.left)
            
