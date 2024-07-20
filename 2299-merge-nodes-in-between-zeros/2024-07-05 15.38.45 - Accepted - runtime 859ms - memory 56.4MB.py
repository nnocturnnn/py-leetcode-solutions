# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        now, nextone = head.next, head.next
        node_sum = 0
        while nextone:
            x = nextone.val
            if x != 0: node_sum += x
            else:
                now.val = node_sum
                now.next = nextone.next
                now = now.next
                node_sum = 0
            nextone = nextone.next
        return head.next
        


            