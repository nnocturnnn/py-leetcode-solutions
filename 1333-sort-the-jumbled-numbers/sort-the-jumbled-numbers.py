class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        converted = []
        for num in nums:
            original_num = num  
            mapped_num = 0
            power_of_ten = 1 
            while num > 0 or power_of_ten == 1:
                num, digit = divmod(num, 10)
                mapped_num = mapping[digit] * power_of_ten + mapped_num
                power_of_ten *= 10
            converted.append(mapped_num)
        return [i for _, i in sorted(enumerate(nums), key=lambda x: (converted[x[0]], x[0]))]