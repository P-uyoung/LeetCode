# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        arr = []
        while head.next :
            arr.append(head)
            head = head.next
            
        cur = head
        while arr:
            cur.next = arr.pop()
            cur = cur.next
        cur.next = None
        return head
            
            
        