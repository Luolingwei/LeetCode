
# 思路: 用Counter对数字个数进行记录，从小到大遍历，每个个数大于0的数字需要相应个数的n+1...n+k匹配

import collections
class Solution:
    def isPossibleDivide(self, nums, k):
        count=collections.Counter(nums)
        keys=sorted(count.keys())
        for n in keys:
            if count[n]>0:
                minus=count[n]
                for i in range(n,n+k):
                    if count[i]<minus:
                        return False
                    count[i]-=minus
        return True

a=Solution()
print(a.isPossibleDivide([1,2,3,3,4,4,5,6],4))
print(a.isPossibleDivide([1,2,3,4],3))