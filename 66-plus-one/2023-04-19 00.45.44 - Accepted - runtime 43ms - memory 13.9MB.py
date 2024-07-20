class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = -1
        carry = 1
        while True:
            try:
                if digits[num] + carry > 9:
                    digits[num] = 0
                    carry = 1
                    num -= 1
                else:
                    digits[num] += carry
                    break
            except IndexError:
                digits.insert(0, 1)
                break
        return digits