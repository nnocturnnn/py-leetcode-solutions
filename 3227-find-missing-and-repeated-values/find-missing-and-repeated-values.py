from itertools import chain
from typing import List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        flat = list(chain.from_iterable(grid))
        n = len(grid)
        expected = set(range(1, n * n + 1))
        actual = set(flat)

        missing = (expected - actual).pop()

        seen = set()
        repeat = None
        for x in flat:
            if x in seen:
                repeat = x
                break
            seen.add(x)

        return [repeat, missing]