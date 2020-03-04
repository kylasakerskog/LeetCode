# 19. Remove Nth Node From End of List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
Runtime: 28 ms, faster than 83.72% of Python3 online submissions for Remove Nth Node From End of List.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Remove Nth Node From End of List.
"""
class Solution: # most clever
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head
"""
Runtime: 32 ms, faster than 57.87% of Python3 online submissions for Remove Nth Node From End of List.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Remove Nth Node From End of List.
"""
"""
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        tmp = ListNode(0)
        tmp.next = head
        length = 1
        node = head
        while node.next != None:
            length += 1
            node = node.next
        i = 0
        if length < 2:
            return head.next
        ret = tmp
        while tmp != None:
            if i == length - n:
                tmp.next = tmp.next.next
                i += 1
                continue
            tmp = tmp.next
            i += 1
            
        return ret.next
"""
