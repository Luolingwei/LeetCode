class Solution:
    def dfs(self,nums,target,start,res,path):
        if target<0:
            return
        if target==0:
            res.append(path)
        for i in range(start,len(nums)):
            self.dfs(nums,target-nums[i],i,res,path+[nums[i]])
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res=[]
        self.dfs(candidates,target,0,res,[])
        return res

a=Solution()
print(a.combinationSum([2,3,6,7],7))
print(a.combinationSum([2,3,5],8))