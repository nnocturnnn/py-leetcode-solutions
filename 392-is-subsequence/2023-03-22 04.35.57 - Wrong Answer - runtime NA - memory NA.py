import queue

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        q1 = queue.Queue()
        [q1.put(i) for i in s]
        print(list(q1.queue))
        [q1.get() for i in t if i in s]
        return q1.empty()
