from itertools import permutations

def find_all_indices(string, substring):
    indices = []
    start_index = 0
    while True:
        index = string.find(substring, start_index)
        if index == -1:
            break
        indices.append(index)
        start_index = index + 1
    return indices

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        all_subs = ["".join(i) for i in permutations(words, len(words))]
        indexes = []
        for i in all_subs:
            if all_ind := find_all_indices(s, i):
                indexes += all_ind
        return set(indexes)