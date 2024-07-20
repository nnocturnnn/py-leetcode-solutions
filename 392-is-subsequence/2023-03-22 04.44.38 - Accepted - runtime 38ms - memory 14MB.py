import queue

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        q1 = queue.Queue()
        [q1.put(i) for i in s]
        for i in t:
            if not q1.empty() and i == q1.queue[0]:
                q1.get()
        return q1.empty()
