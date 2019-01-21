class Solution:
    def dfs(self,nums,target,start,res,path):
        if target<0:
            return
        if target==0:
            res.append(path)
            return
        for i in range(start,len(nums)):
            if i>start and nums[i]==nums[i - 1]:
                continue
            self.dfs(nums,target-nums[i],i+1,res,path+[nums[i]])
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res=[]
        candidates.sort()
        self.dfs(candidates,target,0,res,[])
        return res

a=Solution()
print(a.combinationSum2([10,1,2,7,6,1,5],8))
print(a.combinationSum2([2,5,2,1,2],5))
