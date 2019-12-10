class Solution:
    def generateParenthesis(self, n):
        self.ans=[]
        def generate(l,r,path):
            if l>n or r>n:
                return
            if l==n and r==n:
                self.ans.append(path)
                return
            if l>=r:
                if l==r:
                    generate(l+1,r,path+'(')
                else:
                    generate(l,r+1,path+')')
                    generate(l+1,r,path+'(')
        generate(0,0,"")
        return self.ans

a=Solution()
print(a.generateParenthesis(3))


