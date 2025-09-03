from collections import deque

class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        d = deque()
        for num in nums:
            d.appendleft(0) if num % 2 == 0 else d.append(1)
        return list(d)