class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        def sum_of_bits(n):
            count = 0
            while n:
                count += n & 1
                n >>= 1
            return count

        return sum([num for i, num in enumerate(nums) if k == sum_of_bits(i)])