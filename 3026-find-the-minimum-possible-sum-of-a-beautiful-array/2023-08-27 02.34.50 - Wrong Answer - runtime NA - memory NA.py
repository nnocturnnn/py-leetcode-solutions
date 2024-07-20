class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        memo = {}
    
        def helper(length, current_target):
            if length == 0:
                return 0
            if (length, current_target) in memo:
                return memo[(length, current_target)]

            min_sum = float('inf')
            for num in range(1, current_target + 1):
                if num * 2 != current_target and num != current_target - num:
                    new_target = current_target - num
                    min_sum = min(min_sum, num + helper(length - 1, new_target))

            memo[(length, current_target)] = min_sum
            return min_sum

        return helper(n, target)
        