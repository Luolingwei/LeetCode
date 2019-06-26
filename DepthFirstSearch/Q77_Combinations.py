class Solution:
    # solution 1 dfs
    def combine(self, n,k):
        def dfs(start,path):
            if len(path)==k:
                ans.append(path)
                return
            for i in range(start,n+1):
                dfs(i+1,path+[i])
        ans=[]
        dfs(1,[])
        return ans

    # solution 2 iterative
    # def combine(self, n,k):
    #     ans=[[]]
    #     for _ in range(k):
    #         ans=[path+[i] for path in ans for i in range(path[-1]+1 if path else 1,n+1)]
    #     return ans

a=Solution()
print(a.combine(4,3))
print(a.combine(4,2))
print(a.combine(4,1))