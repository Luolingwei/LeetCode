
# 思路: partition时，将与key相等的数全部放到中间，左边为比key小的数，右边为比key大的数，并返回l1,l2两个index，根据l2-l1判断当前数字是否满足要求
# Time Complexity: n+n/2+n/4+...+1=2n-1

class Solution:
    def majorityElement(self, nums):
        ans = []
        if not nums: return
        target = len(nums) / 3
        self.find(nums, target, ans)
        return ans

    def find(self, nums, target, ans):
        if not nums: return
        low1, low2 = self.partition(nums)
        if low2 - low1 - 1 > target:
            ans.append(nums[low1 + 1])
        self.find(nums[:low1 + 1], target, ans)
        self.find(nums[low2:], target, ans)

    def partition(self, nums):
        low, high = 0, len(nums) - 1
        key = nums[high]
        j, l1, l2 = 0, -1, high + 1
        while j < l2:
            if nums[j] < key:
                l1 += 1
                nums[j], nums[l1] = nums[l1], nums[j]
                j += 1
            elif nums[j] > key:
                l2 -= 1
                nums[j], nums[l2] = nums[l2], nums[j]
            else:
                j += 1
        return l1, l2

a=Solution()
print(a.majorityElement([3,2,3]))
print(a.majorityElement([1,1,1,3,3,2,2,2]))
