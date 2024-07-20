class Solution:
    def count_overlapping(self, string, substring):
        count = 0
        start = 0
        while True:
            start = string.find(substring, start) + 1
            if start > 0:
                count += 1
            else:
                return count

    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count_zf_subarr = 0
        str_nums = ":"
        for i in nums:
            str_nums += f"{i}:"
        for i in range(1,len(nums)):
            print(self.count_overlapping(str_nums, ":0"*i))
            count_zf_subarr += self.count_overlapping(str_nums, ":0"*i)
        return count_zf_subarr