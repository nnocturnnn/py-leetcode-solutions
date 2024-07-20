import functools

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        decode = [first]
        val = first
        for num in encoded:
            val = num ^ val
            decode.append(val)
        return decode