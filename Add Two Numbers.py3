# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = temp = ListNode()
        carry = 0
        while l1 or l2 or carry:
            no1 = l1.val if l1 else 0
            no2 = l2.val if l2 else 0
            total = no1 + no2
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            total = no1 + no2 + carry
            temp.next = ListNode(total%10)
            carry = total // 10
            temp = temp.next
        return res.next
