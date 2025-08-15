# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        if not head or not head.next:
            return True

        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                break
        
        cur=slow
        prev=None
        while cur:
            nex=cur.next
            cur.next=prev
            prev=cur
            cur=nex
        
        while prev:
            if head.val!=prev.val:
                return False
            head=head.next
            prev=prev.next
        return True



        