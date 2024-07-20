class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        answer = True if str(num)[-1] != '0' or num == 0 else False
        return answer