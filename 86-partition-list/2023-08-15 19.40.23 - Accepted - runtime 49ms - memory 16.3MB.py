# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def create_linked_list(self, values):
        dummy_head = ListNode(0)
        current = dummy_head
        for val in values:
            current.next = ListNode(val)
            current = current.next
        return dummy_head.next

    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        smaller_nodes = []
        greater_equal_nodes = []
        
        while head:
            val = head.val
            if val < x:
                smaller_nodes.append(val)
            else:
                greater_equal_nodes.append(val)
            head = head.next
        
        result = smaller_nodes + greater_equal_nodes
        return self.create_linked_list(result)