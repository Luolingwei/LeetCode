# Input: A = [1,1,2,2,3,3,4,4,5,5], target = 8
# Output: 20
# Explanation:
# Enumerating by the values (A[i], A[j], A[k]):
# (1, 2, 5) occurs 8 times;
# (1, 3, 4) occurs 8 times;
# (2, 2, 4) occurs 2 times;
# (2, 3, 3) occurs 2 times.

# 思路1: twoSum升级版，用两个dic分别存储oneSum和twoSum的个数分布，每来一个数n，更新oneSum,twoSum,treeSum+=twoSum[target-n]

# 思路2: 用combinations组合出前两个数i,j, 可以重复取，第三个数k=target-i-j, 有三种情况:
# 1: 3个数相等, 方法数=c[i]*c[i]-1*c[i]-2/6
# 2: 2个数相等, 方法数=c[i]*c[i]-1/2*c[k]
# 3: 都不相等, 方法数=c[i]*c[j]*c[k] 要限制k>i,k>j，防止重复.

import itertools
import collections
class Solution:
    # Solution 1 260 ms
    # def threeSumMulti(self, A, target):
    #     oneSum,twoSum,ans=collections.defaultdict(int),collections.defaultdict(int),0
    #     for i in A:
    #         ans+=twoSum[target-i]
    #         for n,count in oneSum.items():
    #             twoSum[n+i]+=count
    #         oneSum[i]+=1
    #     return ans%(10**9+7)

    # Solution 2 64 ms
    def threeSumMulti(self, A, target):
        c,ans=collections.Counter(A),0
        for i,j in itertools.combinations_with_replacement(c,2):
            k=target-i-j
            if i==j==k: ans+=c[i]*(c[i]-1)*(c[i]-2)/6
            elif i==j!=k: ans+=c[i]*(c[i]-1)/2*c[k]
            elif k>i and k>j: ans+=c[i]*c[j]*c[k]
        return ans%(10**9+7)

a=Solution()
print(a.threeSumMulti([1,1,2,2,3,3,4,4,5,5],8))