# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverseLinkedList(head):
            prev = None
            current = head
            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return prev

        l1 = reverseLinkedList(l1)
        l2 = reverseLinkedList(l2)

        carry = 0
        result_head = ListNode(0)
        current = result_head

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total_sum = val1 + val2 + carry

            carry = total_sum // 10
            current.next = ListNode(total_sum % 10)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        result_head = reverseLinkedList(result_head.next)

        return result_head

    def createLinkedList(values):
        dummy = ListNode(0)
        current = dummy
        for val in values:
            current.next = ListNode(val)
            current = current.next
        return dummy.next

    def linkedListToList(head):
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result







