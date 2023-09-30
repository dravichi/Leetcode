# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merge = head = ListNode()
        while list1 and list2:
            if list1.val > list2.val:
                merge.next = list2
                list2 = list2.next
            else:
                merge.next = list1
                list1 = list1.next
            merge = merge.next
        merge.next = list2 if list2 else list1
        return head.next
           
        
