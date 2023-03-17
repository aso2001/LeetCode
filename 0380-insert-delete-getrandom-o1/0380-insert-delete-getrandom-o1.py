class RandomizedSet:
    def __init__(self):
        self.rndlist = []
        self.rnddict = dict()

    def insert(self, val: int) -> bool:
        if val in self.rnddict:
            return False
        else:
            self.rnddict[val] = len(self.rndlist)
            self.rndlist.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self.rnddict:
            self.rnddict[self.rndlist[-1]] = self.rnddict[val]
            self.rndlist[-1], self.rndlist[self.rnddict[val]] = self.rndlist[self.rnddict[val]], self.rndlist[-1]
            self.rndlist.pop()
            del self.rnddict[val]
            return True
        else:
            return False        

    def getRandom(self) -> int:
        return random.choice(self.rndlist)
    
# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

class RandomizedSet2:

    def __init__(self):
        self.rndset = set()

    def insert(self, val: int) -> bool:
        if val in self.rndset:
            return False
        else:
            self.rndset.add(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self.rndset:
            self.rndset.remove(val)
            return True
        else:
            return False        

    def getRandom(self) -> int:
        return random.sample(self.rndset, 1)[0]