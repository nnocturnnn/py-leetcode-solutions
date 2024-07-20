class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        association = {}
        for letter, world in zip(pattern, s.split()):
            if letter in association and association[letter] != world:
                return False
            association[letter] = world
        return True