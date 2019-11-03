
# 思路: 用HashTable记录从开头到每个位置的odd个数，count[curC-k]为中间odd为k的子数组个数

import collections
class Solution:
    # O(n)
    def numberOfSubarrays(self, nums, k):
        count=collections.defaultdict(int)
        count[0]=1
        curC,ans=0,0
        for n in nums:
            if n%2:
                curC+=1
            ans+=count[curC-k]
            count[curC]+=1
        return ans

a=Solution()
print(a.numberOfSubarrays([1,1,2,1,1],3))
print(a.numberOfSubarrays([2,4,6],1))
