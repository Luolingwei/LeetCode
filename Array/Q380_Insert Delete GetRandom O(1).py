class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.Randomset=set()
        self.length=0

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.Randomset:
            return False
        else:
            self.Randomset.add(val)
            self.length+=1
            return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.Randomset:
            self.Randomset.remove(val)
            self.length-=1
            return True
        else:
            return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        import random
        return list(self.Randomset)[random.randint(0,self.length-1)]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()