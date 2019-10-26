class Solution:
    def TwoSum(self,nums,target):
        ans=0
        memo,pairs=set(),set()
        for n in nums:
            if target-n in memo and n not in pairs:
                ans+=1
                pairs.add(n)
                pairs.add(target-n)
            memo.add(n)
        return ans

a=Solution()
print(a.TwoSum([1, 1, 2, 45, 46, 46],47))
print(a.TwoSum([1, 1],2))
print(a.TwoSum([5, 1, 5, 1, 5],6))