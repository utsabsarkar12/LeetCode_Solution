# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode(0)
        ptr = dummyNode
        carry = 0
        while (l1 or l2 or carry):
            if(l1):
                carry = carry + l1.val
                l1 = l1.next
            elif(l2):
                carry = carry + l2.val
                l2 = l2.next
            ptr.next = ListNode(carry % 10)
            ptr = ptr.next

            carry = carry//10

            return dummyNode.next
