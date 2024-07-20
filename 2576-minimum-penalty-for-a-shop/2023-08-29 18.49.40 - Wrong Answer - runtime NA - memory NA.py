class Solution:
    def bestClosingTime(self, customers: str) -> int:
        def penalty(hours):
            p = 0
            for i in range(len(customers)):
                if customers[i] == 'N' and i < hours:
                    p += 1
                elif customers[i] == 'Y' and i >= hours:
                    p += 1
            return p
        
        n = len(customers)
        left, right = 0, n
        
        while left < right:
            mid = left + (right - left) // 2
            penalty_mid = penalty(mid)
            penalty_mid_plus_one = penalty(mid + 1)
            
            if penalty_mid <= penalty_mid_plus_one:
                right = mid
            else:
                left = mid + 1
        
        return left