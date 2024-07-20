# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], sv: int, dv: int) -> str:
        q = []
        q.append([root, ""])
        p1, p2, p1f, p2f = [], [], False, False
        while len(q) != 0:
            t = q.pop()
            if p1f and p2f:
                break

            if not p1f and t[0].val == sv:
                p1f, p1 = True, t[1]

            if not p2f and t[0].val == dv:
                p2f, p2 = True, t[1]

            if t[0].left != None:
                q.append([t[0].left, t[1] + "L"])
            if t[0].right != None:
                q.append([t[0].right, t[1] + "R"])

        i1, i2 = 0, 0
        while i1 < len(p1) and i2 < len(p2) and p1[i1] == p2[i2]:
            i1, i2 = i1+1, i2+1
        return ''.join("U" for i in range(i1, len(p1))) + ''.join(i for i in p2[i2:])
