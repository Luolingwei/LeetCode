class NestedIterator(object):

    def __init__(self, nestedList):
        self.array = self.flatten(nestedList)
        self.i = 0
        self.length = len(self.array)

    def flatten(self, nestedList):
        ans = []
        for item in nestedList:
            if item.isInteger():
                ans.append(item.getInteger())
            else:
                ans += self.flatten(item.getList())
        return ans

    def next(self):
        """
        :rtype: int
        """
        num = self.array[self.i]
        self.i += 1
        return num

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.i < self.length