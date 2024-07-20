# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        bin_num = ""
        while True:
            bin_num += str(head.val)
            if head.next:
                head = head.next
            else:
                break
        return int(bin_num, 2)