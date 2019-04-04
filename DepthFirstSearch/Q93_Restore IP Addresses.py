class Solution:
    def dfs(self,s,path,length,ans):
        if length==4:
            if not s:
                ans.append(path)
            else:
                return
        for i in range(1,4):
            if i<=len(s):
                if i==1:
                    self.dfs(s[i:],path+[s[:i]],length+1,ans)
                if i==2 and s[0]!='0':
                    self.dfs(s[i:],path+[s[:i]],length+1,ans)
                if i==3 and s[0]!='0' and int(s[:i])<=255:
                    self.dfs(s[i:],path+[s[:i]],length+1,ans)
    def restoreIpAddresses(self, s):
        ans=[]
        self.dfs(s,[],0,ans)
        return ['.'.join(path) for path in ans]

a=Solution()
print(a.restoreIpAddresses("255255255255"))
print(a.restoreIpAddresses("25525511135"))
print(a.restoreIpAddresses("010010"))
