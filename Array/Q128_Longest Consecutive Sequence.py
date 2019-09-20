
# 思路: 建立set，num in set查找的时间复杂度为O(1), 建立set的时间复杂度为O(n)
# 从每条路径的开头开始查找，每次递增1

class Solution:
    def longestConsecutive(self, nums):
        s=set(nums)
        ans=0
        for n in nums:
            if n-1 not in s:
                m=n
                while m+1 in s:
                    m=m+1
                ans=max(ans,m-n+1)
        return ans

a=Solution()
print(a.longestConsecutive([100, 4, 200, 1, 1, 3, 2]))
print(a.longestConsecutive([0]))
print(a.longestConsecutive([]))
print(a.longestConsecutive([1,2,0,1]))