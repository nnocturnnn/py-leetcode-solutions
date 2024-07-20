from itertools import combinations
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digit_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def backtrack(combination, next_digits):
            if not next_digits:
                combinations.append(combination)
                return

            current_digit = next_digits[0]
            letters = digit_to_letters[current_digit]

            for letter in letters:
                backtrack(combination + letter, next_digits[1:])

        combinations = []
        backtrack('', digits)
        return combinations
            
        
