from heapq import heappush, heappop
from collections import Counter

class Key:
    def __init__(self, character: str, freq: int) -> None:
        self.character = character
        self.freq = freq
 
    def __lt__(self, other: "Key") -> bool:
        return self.freq > other.freq

class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        count = Counter(s)
        pq = []
        
        for c, freq in count.items():
            heappush(pq, Key(c, freq))
    
        prev = Key('', 0)
        result = []
    
        while pq:
            key = heappop(pq)
            result.append(key.character)
    
            key.freq -= 1
    
            if prev.freq > 0:
                heappush(pq, prev)
    
            prev = key
    
        if len(result) != n:
            return ""
        else:
            return ''.join(result)
