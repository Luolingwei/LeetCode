
# 思路: sliding window, 在sliding的过程中要记录window中的最大最小值, 用单调队列
# maxq(单调递减)和minq(单调递增)分别记录window中的最大值和最小值candidates.
# 当最大值与最小值的差大于limite时, 说明nums[j]更新了最大值或最小值, 此时需要移动i到最大值位置+1/最小值位置+1

from collections import deque
class Solution:
    # O(n)
    def longestSubarray(self, nums, limit: int) -> int:
        i = 0
        N = len(nums)
        maxq,minq = deque(),deque()
        ans = 0
        for j in range(N):
            while maxq and nums[j]>nums[maxq[-1]]: maxq.pop()
            while minq and nums[j]<nums[minq[-1]]: minq.pop()
            maxq.append(j)
            minq.append(j)
            while nums[maxq[0]]-nums[minq[0]]>limit:
                if nums[j]==nums[maxq[0]]:
                    i = minq.popleft()+1
                else:
                    i = maxq.popleft()+1
            ans = max(ans,j-i+1)
        return ans

a=Solution()
print(a.longestSubarray([8,2,4,7],4))
print(a.longestSubarray([10,1,2,4,7,2],5))
print(a.longestSubarray([4,2,2,2,4,4,2,2],0))