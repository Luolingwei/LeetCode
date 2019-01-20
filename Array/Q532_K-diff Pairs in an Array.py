import collections
class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count=0
        if k<0:
            return 0
        if k==0:
            counter=collections.Counter(nums)
            for key,value in counter.items():
                if value>=2:
                    count+=1
            return count
        nums=set(nums)
        for num in nums:
            if num+k in nums:
                count+=1
        return count

a=Solution()
print(a.findPairs([3, 1, 4, 1, 5],2))
print(a.findPairs([1, 2, 3, 4, 5],1))
print(a.findPairs([1, 3, 1, 5, 4],0))
print(a.findPairs([1, 1, 1, 1, 1],0))
print(a.findPairs([-1, -2, -3],1))