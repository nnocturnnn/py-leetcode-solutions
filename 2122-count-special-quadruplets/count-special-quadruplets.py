from itertools import combinations 

class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        return sum([1 for i in combinations(nums, 4) if i[0] + i[1] + i[2] == i[3]])
            
