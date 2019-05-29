
# Window position                Median
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       1
#  1 [3  -1  -3] 5  3  6  7       -1
#  1  3 [-1  -3  5] 3  6  7       -1
#  1  3  -1 [-3  5  3] 6  7       3
#  1  3  -1  -3 [5  3  6] 7       5
#  1  3  -1  -3  5 [3  6  7]      6

# 思路: 保持window为有序序列.并依次算median
# median的算法注意用 (window[k//2]+window[-(k//2+1)])/2，简单高效

import bisect
class Solution:
    def medianSlidingWindow(self, nums, k):
        window=sorted(nums[:k])
        median=[(window[k//2]+window[-(k//2+1)])/2]
        for i in range(k,len(nums)):
            window.remove(nums[i-k])
            bisect.insort(window,nums[i])
            median+=[(window[k//2]+window[-(k//2+1)])/2]
        return median

a=Solution()
print(a.medianSlidingWindow([1,3,-1,-3,5,3,6,7],3))