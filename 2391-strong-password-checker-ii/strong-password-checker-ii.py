import string

class Solution:
    def strongPasswordCheckerII(self, s: str) -> bool:
        return (
            len(s) > 7
            and not any(s[i] == s[i-1] for i in range(1, len(s)))
            and bool(set(s) & set(string.ascii_lowercase))
            and bool(set(s) & set(string.ascii_uppercase))
            and bool(set(s) & set(string.digits))
            and bool(set(s) & set("!@#$%^&*()-+"))
        )