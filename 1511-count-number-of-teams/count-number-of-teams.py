class Solution:
    def factorial_recursive(self,n):
        if n < 0:
            return 0
        if n == 0 or n == 1:
            return 1
        else:
            return n * self.factorial_recursive(n - 1)

    def numTeams(self, rating: List[int]) -> int:
        count = 0
        
        for i in range(len(rating)):
            ans_1 = 0
            ans_2 = 0
            for j in range(0,i):
                if rating[j] < rating[i]:
                    ans_1 += 1
            for j in range(i,len(rating)):
                if rating[j] > rating[i]:
                    ans_2 += 1
            count += ans_1 * ans_2

        for i in range(len(rating)):
            ans_1 = 0
            ans_2 = 0
            for j in range(0,i):
                if rating[j] > rating[i]:
                    ans_1 += 1
            for j in range(i,len(rating)):
                if rating[j] < rating[i]:
                    ans_2 += 1
            count += ans_1 * ans_2
        
        return count
        