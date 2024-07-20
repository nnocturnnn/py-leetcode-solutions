class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        reordered = [None] * len(nums)
        even_index = 0
        odd_index = len(nums) - 1

        for num in nums:
            if num % 2 == 0:
                reordered[even_index] = num
                even_index += 1
            else:
                reordered[odd_index] = num
                odd_index -= 1

        return reordered