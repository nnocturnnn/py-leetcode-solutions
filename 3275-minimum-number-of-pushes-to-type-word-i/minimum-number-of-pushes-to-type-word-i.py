class Solution:
    def minimumPushes(self, word: str) -> int:
        lst = []
        c = 0

        for i in word:
            if len(lst) < 8:
                if i not in lst:
                    lst.append(i)
                    c += 1
                else:
                    c += 1
            else:
                m = (lst.index(i) // 8) + 1 if i in lst else (len(lst) // 8) + 1
                print(m)
                if i not in lst:
                    lst.append(i)
                    c += m
                else:
                    c += m

        return c