# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        if '[' not in s:
            return NestedInteger(int(s))
        stack = []
        sign = 1
        num = None
        for ch in s:
            if ch == '-':
                sign = -1
            elif ch == ',':
                if num is not None:
                    stack[-1].add(NestedInteger(sign * num))
                    sign = 1
                    num = None
            elif ch == '[':
                stack.append(NestedInteger())
            elif ch == ']':
                if num is not None:
                    stack[-1].add(NestedInteger(sign * num))
                    sign = 1
                    num = None
                _list = stack.pop()
                if stack:
                    stack[-1].add(_list)
                else:
                    return _list
            else:
                num = num * 10 + int(ch) if num else int(ch)
        