# Input: A = [1,0,1,0,1], S = 2
# Output: 4
# Explanation:
# The 4 subarrays are bolded below:
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]

# 思路:和Q437 Path Sum 3 思路一样，记录当前的curS，如果curS-target在dic中，则加上其count

import collections
class Solution:
    def numSubarraysWithSum(self, A, S):
        dic,ans,curS=collections.defaultdict(int),0,0
        dic[0]=1
        for num in A:
            curS+=num
            ans+=dic[curS-S]
            dic[curS]+=1
        return ans

a=Solution()
print(a.numSubarraysWithSum([1,0,1,0,1],2))
print(a.numSubarraysWithSum([1,0,1,3,1],5))