import bisect

# 思路: 把nums1 sort, 对于每个nums1[i], 找nums1中和nums2[i]最接近的数字
# gain = 原diff(nums1[i]-nums2[i]) - 新diff(nums[idx]-nums2[i])
# 找出最大的gain即可, 可能为0

class Solution:
    def minAbsoluteSumDiff(self, nums1, nums2):
        nums1_sort = sorted(nums1)
        N = len(nums1)
        gain, total_diff, mod = 0, 0, 10 ** 9 + 7
        for i in range(N):
            curDiff = abs(nums1[i] - nums2[i])
            total_diff = (total_diff + curDiff) % mod
            idx = bisect.bisect_left(nums1_sort, nums2[i])
            if idx < N: gain = max(gain, curDiff - abs(nums1_sort[idx] - nums2[i]))
            if idx - 1 >= 0: gain = max(gain, curDiff - abs(nums1_sort[idx - 1] - nums2[i]))
        return (total_diff - gain) % mod


a=Solution()
print(a.minAbsoluteSumDiff([1,7,5], [2,3,5]))
print(a.minAbsoluteSumDiff([2,4,6,8,10], [2,4,6,8,10]))
print(a.minAbsoluteSumDiff([1,10,4,4,2,7], [9,3,5,1,7,4]))