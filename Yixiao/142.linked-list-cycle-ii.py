#
# @lc app=leetcode id=142 lang=python
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if(head == None):
            return None

        slow = head
        fast = head

        while True:
            if(fast.next == None or fast.next.next == None):
                return None
            fast = fast.next.next
            slow = slow.next
            if(fast == slow):
                break
        
        fast = head
        while(fast != slow):
            fast = fast.next
            slow = slow.next
        return fast
        
# @lc code=end

