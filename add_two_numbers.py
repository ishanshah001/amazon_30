# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        total = ListNode()
        curr = total
        sum = 0
        while l1 or l2 or carry:
            sum = carry
            if l1:
                sum = sum + l1.val
                l1 = l1.next
            if l2:
                sum = sum +l2.val
                l2 = l2.next
            carry = sum//10
            num = sum%10
            curr.next = ListNode(num)
            curr = curr.next
        
        return total.next