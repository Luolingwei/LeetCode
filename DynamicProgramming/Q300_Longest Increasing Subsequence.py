import bisect
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = []
        for num in nums:
            bi = bisect.bisect_left(dp,num)
            if bi == len(dp):
                dp += [num]
            else:
                dp[bi] = num
        return len(dp)

a=Solution()
print(a.lengthOfLIS([10,9,2,5,3,8,101,6,7]))