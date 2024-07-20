class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        delimeter = 3
        out = []
        helper = []
        for num in nums:
            delimeter -= 1
            helper.append(num)
            if not delimeter:
                if max(helper) - min(helper) > k:
                    return []
                out.append(helper)
                delimeter = 3
                helper = []   
        return out
                

            
