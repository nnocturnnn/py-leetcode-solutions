class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        while True:
            if num == 0:
               return count
            if num % 2 == 0:
                num /= 2
            else:
                num -= 1
            count += 1 
        