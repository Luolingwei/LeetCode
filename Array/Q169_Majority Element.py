# import collections
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # count=collections.Counter(nums)
        # return max(count,key=count.get)
        count={}
        for number in nums:
            count[number]=count.get(number,0)+1
        return max(count,key=count.get)
a=Solution()
print(a.majorityElement([2,2,1,1,1,2,2]))
print(a.majorityElement([3,2,3]))