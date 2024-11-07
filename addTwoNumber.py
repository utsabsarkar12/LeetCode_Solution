# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        ptr = dummyHead
        carry = 0

        while l1 or l2 or carry:
            value1 = l1.val if l1 else 0
            value2 = l2.val if l2 else 0

            carry, sumValue = divmod(value1 + value2 + carry, 10)

            ptr.next = ListNode(sumValue)
            ptr = ptr.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummyHead.next
            