import queue

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        q1 = queue.Queue()
        [q1.put(i) for i in s]
        for i in t:
            if i in s:
                if q1.get() != i:
                    q1.put(i)
        return q1.empty()
