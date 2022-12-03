# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head == None or head.next == None:
            return head
        
        list = head
        
        while(list.next!=None):
            if list.val == list.next.val:
                list.next = list.next.next
            else:
                list = list.next
        
        return head