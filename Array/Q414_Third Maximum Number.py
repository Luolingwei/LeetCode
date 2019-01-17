class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #solution1 using sorted
        # new_nums=sorted(list(set(nums)),reverse=True)
        # return new_nums[2] if len(new_nums)>=3 else new_nums[0]

        #solution2 without sorted
        new_nums=set(nums)
        biggest=max(new_nums)
        new_nums.remove(biggest)
        if len(new_nums)<2:
            return biggest
        else:
            new_nums.remove(max(new_nums))
            return max(new_nums)

a=Solution()
print(a.thirdMax([3, 2, 1]))
print(a.thirdMax([1, 2]))
print(a.thirdMax([2, 2, 3, 1]))
print(a.thirdMax([1, 1, 2]))