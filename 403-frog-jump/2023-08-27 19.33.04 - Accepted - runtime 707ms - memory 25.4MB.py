class Solution:
    def canCross(self, stones: List[int]) -> bool:
        memo = {}
        def helper(position, jump):
            if position == stones[-1]:
                return True
            
            if (position, jump) in memo:
                return memo[(position, jump)]
            
            for next_jump in [jump - 1, jump, jump + 1]:
                if next_jump > 0 and position + next_jump in stones:
                    if helper(position + next_jump, next_jump):
                        memo[(position, jump)] = True
                        return True
            
            memo[(position, jump)] = False
            return False
        
        return helper(0, 0)
        