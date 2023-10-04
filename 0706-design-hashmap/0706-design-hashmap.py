class MyHashMap:

    def __init__(self):
        self.myHash = [-1] * 10000000
        

    def put(self, key: int, value: int) -> None:
        self.myHash[key]=value
        

    def get(self, key: int) -> int:
        
        return self.myHash[key]

    def remove(self, key: int) -> None:
        self.myHash[key] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)