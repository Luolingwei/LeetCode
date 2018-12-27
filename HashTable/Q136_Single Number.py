import collections
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic=collections.Counter(nums)
        for key,value in dic.items():
            if value==1:
                return key
a=Solution()
print(a.singleNumber([4,1,2,1,2]))