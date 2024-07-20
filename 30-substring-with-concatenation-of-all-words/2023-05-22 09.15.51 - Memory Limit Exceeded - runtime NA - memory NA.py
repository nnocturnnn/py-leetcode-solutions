from itertools import permutations

def find_all_indices(string, substring):
    start_index = 0
    while True:
        index = string.find(substring, start_index)
        if index == -1:
            return
        yield index
        start_index = index + 1

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        indexes = []
        word_permutations = set("".join(p) for p in permutations(words))
        
        for perm in word_permutations:
            indices = find_all_indices(s, perm)
            indexes.extend(indices)
        return indexes