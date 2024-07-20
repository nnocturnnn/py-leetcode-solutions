class MyHashMap:

    def __init__(self):
        self.hm = [None] * 10

    def put(self, key: int, value: int) -> None:
        self.hm[key % 10] = value
        
    def get(self, key: int) -> int:
        return self.hm[key % 10] if self.hm[key % 10] else -1 
        
    def remove(self, key: int) -> None:
        self.hm[key % 10] = 0
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)