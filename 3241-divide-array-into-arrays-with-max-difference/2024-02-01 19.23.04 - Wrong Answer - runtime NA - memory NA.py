class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        if max([abs(j - i) for i, j in zip(nums[:-1], nums[1:])]) > k:
            return []
        delimeter = 3
        out = []
        helper = []
        for num in nums:
            delimeter -= 1
            helper.append(num)
            if not delimeter:
                out.append(helper)
                delimeter = 3
                helper = []
        
        return out
                

            
