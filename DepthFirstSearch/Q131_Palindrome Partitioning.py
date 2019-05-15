class Solution:
    def IsPal(self,s):
        return s[::-1]==s
    def dfs(self,s,path,ans):
        if not s:
            ans.append(path)
            return
        for i in range(1,len(s)+1):
            if self.IsPal(s[:i]):
                self.dfs(s[i:],path+[s[:i]],ans)
    def partition(self, s):
        ans=[]
        self.dfs(s,[],ans)
        return ans

a=Solution()
print(a.partition("aab"))