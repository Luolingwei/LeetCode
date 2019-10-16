class Solution:
    def divide(self,n,k):
        s,ans=str(n),set()
        r=k
        while r<=len(s):
            window=s[r-k:r]
            if window[0]!='0' and n%int(window)==0:
                ans.add(window)
            r+=1
        return len(ans)

a=Solution()
print(a.divide(120,2))
print(a.divide(555,1))
print(a.divide(2345,2))
print(a.divide(100,1))
print(a.divide(102,2))