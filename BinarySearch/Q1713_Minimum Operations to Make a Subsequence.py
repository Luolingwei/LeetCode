
# 思路: 可以使用LCS解决, 找到最长的common subsequence即可, O(n^2)
# 但是这里target 是distinct的, 所以可以将数字转为index, 找到对应index的LIS(longest increasing subsequence)即可，O(nlogn)

import bisect
class Solution:
    def minOperations(self, target, arr):
        memo = {n:i for i,n in enumerate(target)}
        q=[]
        for n in arr:
            if n in memo:
                pos = memo[n]
                idx=bisect.bisect_left(q,pos)
                if idx==len(q):
                    q.append(pos)
                else:
                    q[idx]=pos
        return len(target) - len(q)

a = Solution()
print(a.minOperations([5,1,3], [9,4,2,3,4]))
print(a.minOperations([6,4,8,1,3,2], [4,7,6,2,3,8,6,1]))