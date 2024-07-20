# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        index_nodes = []
        if not head.next or not head.next.next:
            return [-1, -1]
        index = 2
        while head.next.next:
            if (head.next.val > head.val and head.next.val > head.next.next.val) or\
                (head.next.val < head.val and head.next.val < head.next.next.val):
                index_nodes.append(index)
            head = head.next
            index += 1

        if len(index_nodes) < 2: return [-1, -1]
        differences = [index_nodes[i+1] - index_nodes[i] for i in range(len(index_nodes) - 1)]
        return [min(differences), index_nodes[-1] - index_nodes[0]]

        