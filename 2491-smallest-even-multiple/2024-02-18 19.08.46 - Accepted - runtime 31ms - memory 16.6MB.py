class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        answer = n if n % 2 == 0 else n*2
        return answer
            