class Solution:
    def sum(self,s1,s2):
        ans=""
        stack1,stack2=[i for i in s1],[j for j in s2]
        while stack1 or stack2:
            cur=int((stack1 or ["0"]).pop())+int((stack2 or ["0"]).pop())
            ans=str(cur)+ans
        return ans

a=Solution()
print(a.sum("99","99"))
print(a.sum("99","1"))
print(a.sum("1092","0"))
