# Input: nums = [1,3], n = 6
# Output: 1
# Explanation:
# Combinations of nums are [1], [3], [1,3], which form possible sums of: 1, 3, 4.
# Now if we add/patch 2 to nums, the combinations are: [1], [2], [3], [1,3], [2,3], [1,2,3].
# Possible sums are 1, 2, 3, 4, 5, 6, which now covers the range [1, 6].
# So we only need 1 patch.

# 思路: 类似于dp，设置一个能到达的最大值(开区间，该数不可达)，每次插入一个数组中的数就对其更新，当插入的数小于等于这个最大值时，将可达范围扩展至max+nums[i]，因为max到max+nums[i]之间的数都能被合成
# 当插入的数小于可达范围时，必须要插入最大值，使得范围能继续扩大到max+max，（如果插入的值大于最大值，那么插入值和最大值之间的数将变得不可达），此时没用数组中的数扩大范围,所以不更新i,留着继续用来扩大范围
# 结束条件为一直到可达范围达到目标


class Solution:
    def minPatches(self, nums, n):
        i,max_range,count=0,1,0
        while max_range<n+1:
            if i<len(nums) and nums[i]<=max_range:
                max_range+=nums[i]
                i+=1
            else:
                max_range+=max_range
                count+=1
        return count


a=Solution()
print(a.minPatches([1,3],6))
print(a.minPatches([1,5,10],20))
print(a.minPatches([1,5,10],20))
print(a.minPatches([1,2,4,13,43],100))
print(a.minPatches([],10))