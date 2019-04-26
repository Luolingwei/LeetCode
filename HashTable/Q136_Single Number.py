
# Given a non-empty array of integers, every element appears twice except for one. Find that single one.
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

# Input: [2,2,1]
# Output: 1
#
# Input: [4,1,2,1,2]
# Output: 4

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