# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        def find_length(node):
            length = 0
            while node:
                length += 1
                node = node.next
            return length

        ll_len = find_length(head)
        sublist_length = ll_len // k
        remainder = ll_len % k

        result = [None] * k
        current = head
        prev = None

        for i in range(k):
            result[i] = current
            sublist_size = sublist_length + (1 if i < remainder else 0)

            for j in range(sublist_size):
                prev = current
                current = current.next

            if prev:
                prev.next = None

        return result