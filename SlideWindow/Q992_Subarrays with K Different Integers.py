import collections

class Solution:
    '''
    subarray at most K distinct:
    r from 0 to length-1, ans+=r-l+1, when distinct(K)<0, move l to right.
    return subarray at most K distinct-subarray at most K-1 distinct
    '''

    def subarraysWithKDistinct(self, nums, K):
        return self.AtMostK(nums, K) - self.AtMostK(nums, K - 1)

    def AtMostK(self, nums, K):
        N = len(nums)
        l, res = 0, 0
        count = collections.Counter()
        for r in range(N):
            if not count[nums[r]]:
                K -= 1
            count[nums[r]] += 1
            while K < 0:
                count[nums[l]] -= 1
                if not count[nums[l]]:
                    K += 1
                l += 1
            res += r - l + 1
        return res