class Solution:
    def generate(self,left,right,path,ans):
        if left: self.generate(left-1,right,path+'(',ans)
        if right>left: self.generate(left,right-1,path+')',ans)
        if not right: ans.append(path)
        return ans

    def generateParenthesis(self, n):
        return self.generate(n,n,'',[])

a=Solution()
print(a.generateParenthesis(3))


