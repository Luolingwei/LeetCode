# [0 ,0, 0, 1, 2, 2]; target = 2, 要return [[0, 2], [0, 2]]

import collections
class Solution:
    # Solution 1 HashTable O(n)
    def find(self,nums,target):
        ans=[]
        memo=collections.Counter()
        for n in nums:
            if memo[target-n]>0:
                ans.append([n,target-n])
                memo[target-n]-=1
            else:
                memo[n]+=1
        return ans

    # Solution 2 Two pointers O(nlogn)
    # def find(self,nums,target):
    #     nums.sort()
    #     ans=[]
    #     l,r=0,len(nums)-1
    #     while l<r:
    #         curS=nums[l]+nums[r]
    #         if curS==target:
    #             ans.append([nums[l],nums[r]])
    #             l+=1
    #             r-=1
    #         elif curS>target:
    #             r-=1
    #         else:
    #             l+=1
    #     return ans


a=Solution()
print(a.find([0 ,0, 0, 1, 1, 2, 2],0))