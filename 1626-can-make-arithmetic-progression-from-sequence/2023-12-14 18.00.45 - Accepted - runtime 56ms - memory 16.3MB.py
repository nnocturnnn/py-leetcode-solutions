class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        sorted_numbers = sorted(arr)
        return all(sorted_numbers[i] - sorted_numbers[i-1] == sorted_numbers[1] - sorted_numbers[0] for i in range(1, len(sorted_numbers)))
        