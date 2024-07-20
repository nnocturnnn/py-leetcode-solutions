class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if sum(bytearray(s,encoding='utf8')) == sum(bytearray(goal,encoding='utf8')):
            if sum(0 if i == j else 1 for i, j in zip(s, goal)) > 2:
                return False
            else:
                return True
        else:
            return False