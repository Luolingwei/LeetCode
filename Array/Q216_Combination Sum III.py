class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        ans=[]
        self.dfs(k,n,[],ans,1)
        return ans

    def dfs(self,k,n,solution,ans,start):
        if k==0 and n==0:
            ans.append(solution[:])
            return
        else:
            for i in range(start,10):
                solution.append(i)
                self.dfs(k-1,n-i,solution,ans,i+1)
                solution.pop()

a=Solution()
print(a.combinationSum3(3,9))
print(a.combinationSum3(2,10))