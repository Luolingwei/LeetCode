class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict_nums={}
        for i, value in enumerate(nums):
            if target-value in dict_nums.keys():
                return [i,dict_nums[target-value]]
            else:
                dict_nums[value]=i

s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))
print(s.twoSum([3, 2, 4], 6))
print(s.twoSum([3, 3], 6))