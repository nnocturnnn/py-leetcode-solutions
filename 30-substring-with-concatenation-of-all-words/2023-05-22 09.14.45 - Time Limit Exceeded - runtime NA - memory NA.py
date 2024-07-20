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
        indexes = set()
        for perm in permutations(words, len(words)):
            perm_str = "".join(perm)
            indices = find_all_indices(s, perm_str)
            if indices:
                indexes.update(indices)
        return indexes