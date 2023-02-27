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
        def flatten(listt):
            temp = []
            for i in listt:
                if i.isInteger():
                    temp.append(i.getInteger())
                else:
                    temp.extend(flatten(i.getList()))
            return temp
        
        self.arr = flatten(nestedList)
        self.itr = -1
        
            
    def next(self) -> int:
        self.itr += 1
        return self.arr[self.itr]
    
    def hasNext(self) -> bool:
         return self.itr < len(self.arr) - 1


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())