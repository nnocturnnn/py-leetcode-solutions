class Solution:
    def count_overlapping(self, nums, subarray):
        count = 0
        for i in range(len(nums)-len(subarray)+1):
            if nums[i:i+len(subarray)] == subarray:
                count += 1
        return count

    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count_zf_subarr = 0
        for i in range(1,len(nums)+1):
            count_zf_subarr += self.count_overlapping(nums, [0]*i)
        return count_zf_subarr