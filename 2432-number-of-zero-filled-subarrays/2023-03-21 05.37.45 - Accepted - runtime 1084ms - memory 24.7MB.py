from collections import defaultdict

class Solution:
            
    def zeroFilledSubarray(self, nums):
        count=0
        sub=0
        for i in nums:
            if i == 0:
                sub+=1
            else:
                sub=0
            count+=sub
        return count