class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        sabp = []
        [sabp.insert(0, i) if i % 2 == 0 else sabp.append(i) for i in nums]
        return sabp