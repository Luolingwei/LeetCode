# Input: nums = [3, 4, 2]
# Output: 6
# Explanation:
# Delete 4 to earn 4 points, consequently 3 is also deleted.
# Then, delete 2 to earn 2 points. 6 total points are earned.

# 思路: dp, 与House Robber类似，但是这里的数字并不是连续的，并且只有两个key相邻的时候才不能连续取数.
# 所以这里用prev和cur分别记录上一个和上上一个的max值. 如果当前key和上一个key相差1:当前max等于max(cur,prev+dic[n]*n)，如果相差大于1: 当前max=cur+dic[n]*n

import collections

class Solution:
    def deleteAndEarn(self, nums):
        if not nums: return 0
        dic=collections.Counter(nums)
        keys=sorted(dic.keys())
        cur,prev=dic[keys[0]]*keys[0],0
        for i in range(1,len(keys)):
            if keys[i]-keys[i-1]==1:
                cur,prev=max(cur,prev+dic[keys[i]]*keys[i]),cur
            else:
                cur,prev=cur+dic[keys[i]]*keys[i],cur
        return cur

a=Solution()
print(a.deleteAndEarn([]))
print(a.deleteAndEarn([3, 1]))
print(a.deleteAndEarn([3, 4, 2]))
print(a.deleteAndEarn([2, 2, 3, 3, 3, 4]))