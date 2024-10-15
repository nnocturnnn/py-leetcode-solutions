from collections import Counter 

class Solution:
    def equalFrequency(self, word: str) -> bool:
        counter = Counter(word)
        for char in counter:
            new_counter = Counter(word.replace(char, '', 1))
            if len(set(new_counter.values())) == 1:
                return True
        
        return False
        