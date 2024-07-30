class Solution:
    def minimumDeletions(self, s: str) -> int:
        count_b=0
        deletion=0
        for i in s:
            if i=='a':
                deletion=min(deletion+1,count_b)    
            else:
                count_b+=1
            
        return deletion