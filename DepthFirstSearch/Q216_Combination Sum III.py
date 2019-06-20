class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        def dfs(k,n,path,start):
            if k<=0 or n<=0:
                if k==0 and n==0:ans.append(path[:])
                else: return
            for i in range(start,10):
                path.append(i)
                dfs(k-1,n-i,path,i+1)
                path.remove(i)
        ans=[]
        dfs(k,n,[],1)
        return ans

a=Solution()
print(a.combinationSum3(3,9))
print(a.combinationSum3(2,10))