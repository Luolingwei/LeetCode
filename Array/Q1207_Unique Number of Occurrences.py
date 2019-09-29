
import collections
class Solution:
    def uniqueOccurrences(self, arr):
        C=collections.Counter(arr)
        return len(set(C.values()))==len(C.values())

a=Solution()
print(a.uniqueOccurrences([1,2,2,1,1,3]))
print(a.uniqueOccurrences([1,2]))