import collections
class Solution:
    def findLHS(self, nums):
        longest=0
        counter=collections.Counter(nums)
        for key,value in counter.items():
            if key+1 in counter:
                longest=max(longest,counter[key]+counter[key+1])
        return longest

a=Solution()
print(a.findLHS([]))
print(a.findLHS([1,3,2,2,5,2,3,7]))
print(a.findLHS([1,1,3,3,5,5,5]))
print(a.findLHS([1,1,1,1]))