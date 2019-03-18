class Solution:
    # solution 1 dfs
    # def dfs(self,start,path,ans,n,k):
    #     if len(path)==k:
    #         ans.append(path)
    #         return
    #     for i in range(start,n+1):
    #         self.dfs(i+1,path+[i],ans,n,k)
    # def combine(self, n,k):
    #     ans=[]
    #     self.dfs(1,[],ans,n,k)
    #     return ans

    # solution 2 iterative
    def combine(self, n,k):
        ans=[[]]
        for _ in range(k):
            ans=[path+[i] for path in ans for i in range(path[-1]+1 if path else 1,n+1)]
        return ans

a=Solution()
print(a.combine(4,3))
print(a.combine(4,2))
print(a.combine(4,1))