from itertools import permutations
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        all_subs = ["".join(i) for i in permutations(words, len(words))]
        print(all_subs)
        return [s.find(i) for i in all_subs if i in s]