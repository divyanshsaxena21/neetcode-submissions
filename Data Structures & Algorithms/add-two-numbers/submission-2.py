# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    
        num1 = 0
        place = 1

        while l1:
            num1 += l1.val * place
            place *= 10
            l1 = l1.next

        num2 = 0
        place = 1

        while l2:
            num2 += l2.val * place
            place *= 10
            l2 = l2.next

        num1 = num1 + num2

        if num1 == 0:
            return ListNode(0)

        newHead = None
        tail = None

        while num1:
            r = num1 % 10
            num1 //= 10

            newNode = ListNode(r)

            if newHead is None:
                newHead = newNode
                tail = newNode
            else:
                tail.next = newNode
                tail = tail.next

        return newHead
