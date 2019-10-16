class Solution:
    def check(self,s1,s2):
        def helper(A,B,signal):
            ans=0
            for i,c in enumerate(A):
                if c.isdigit():
                    curS=A[:i]+A[i+1:]
                    if signal:
                        if curS<B:
                            ans+=1
                    else:
                        if curS>B:
                            ans+=1
            return ans
        return helper(s1,s2,1)+helper(s2,s1,0)

a=Solution()
print(a.check("abc12f","9de83jdf"))
print(a.check("wbc12f","9de83jdf"))