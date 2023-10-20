# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.tmp = []
        self.idx = 0
        self.flatten_list(nestedList)
    
    def next(self) -> int:
        res = self.tmp[self.idx]
        self.idx += 1
        return res
    
    def hasNext(self) -> bool:
        return self.idx < len(self.tmp)
    
    def flatten_list(self, nestedList):
        for i in nestedList:
            if i.isInteger():
                self.tmp.append(i.getInteger())
            else:
                self.flatten_list(i.getList())

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())