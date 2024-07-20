class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        keys = {"type" : 0, "color" : 1, "name" : 2}
        return sum([1 for i in items if i[keys[ruleKey]] == ruleValue])
        