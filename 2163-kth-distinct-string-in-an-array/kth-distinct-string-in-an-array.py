from collections import Counter

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        for item, count in Counter(arr).items():
            if count == 1:
                k -= 1
                if k == 0:
                    return item
        return ""