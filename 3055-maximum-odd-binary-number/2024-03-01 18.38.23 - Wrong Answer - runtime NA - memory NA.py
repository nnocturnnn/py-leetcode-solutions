from itertools import combinations

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        if s[-1] == '1':
            return s
        # If it's even, find the rightmost '1' to ensure the largest odd number
        else:
            rightmost_one = s.rfind('1')
            if rightmost_one != -1:
                # Return up to the rightmost '1' to make it the largest odd number
                return s[:rightmost_one+1]
            else:
                # If there are no '1's, it's not possible to form an odd number
                return '0'