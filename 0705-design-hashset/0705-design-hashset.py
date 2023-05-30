class MyHashSet:

    def __init__(self):
        self.hm = [False]*1000001

    def add(self, key: int) -> None:
        if not self.hm[key]: self.hm[key] = True

    def remove(self, key: int) -> None:
        if self.hm[key]: self.hm[key] = False

    def contains(self, key: int) -> bool:
        if self.hm[key]: return True
        else: return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)