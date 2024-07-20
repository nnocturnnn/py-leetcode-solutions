from itertools import combinations

class Solution:

    def allSubArrays(self,xs):
        n = len(xs)
        indices = list(range(n+1))
        for i,j in combinations(indices,2):
            yield xs[i:j]
            
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count = 0
        for i in self.allSubArrays(nums):
            if not any(i):
                print(i)
                count += 1
        return count