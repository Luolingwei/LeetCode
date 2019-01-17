import collections
class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #solution1
        # ans,dic=set(),set()
        # for num in nums:
        #     if num in dic:
        #         ans.add(num)
        #     else:
        #         dic.add(num)
        # return list(ans)

        #solution2
        return [num for num, n in collections.Counter(nums).items() if n==2]

a=Solution()
print(a.findDuplicates([4,3,2,7,8,2,3,1]))