# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        
        if not list2:
            return list1
        
        dummy = ListNode()
        head = ListNode()
        dummy.next = head
        l1 = list1
        l2 = list2

        while l1 and l2:
            if l1.val<l2.val:
                head.next = l1
                head = head.next
                l1 = l1.next
            else:
                head.next = l2
                head = head.next
                l2 = l2.next
        
        while l1:
            head.next = l1
            l1 = l1.next
            head = head.next

        while l2:
            head.next = l2
            l2 = l2.next
            head = head.next
        
        return dummy.next.next
        

            
            

