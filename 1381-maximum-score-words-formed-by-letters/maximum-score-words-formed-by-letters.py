from collections import Counter

ASCII_A = ord('a')

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        letter_count = Counter(letters)
        letter_score = {chr(index + ASCII_A): weight for index, weight in enumerate(score)}

        def calculate_score(word):
            return sum(letter_score[char] for char in word)
        
        max_score = 0
        for r in range(1, len(words) + 1):
            for word_combo in combinations(words, r):
                combined_letter_count = Counter("".join(word_combo))
                if all(combined_letter_count[char] <= letter_count[char] for char in combined_letter_count):
                    combo_score = sum(calculate_score(word) for word in word_combo)
                    max_score = max(max_score, combo_score)
        
        return max_score