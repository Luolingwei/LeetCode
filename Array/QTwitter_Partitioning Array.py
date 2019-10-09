
# 思路: check最大的数字个数即可

import collections
class Solution:
    def partition(self,nums,k):
        if not nums or not k: return False
        if len(nums)%k!=0: return False
        c=collections.Counter(nums)
        if max(c.values())>len(nums)//k: return False
        return True

a=Solution()
print(a.partition([1,2,3],1))