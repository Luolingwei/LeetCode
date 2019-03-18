class Solution:
    def generate(self,strs):
        key,num,ans='',0,''
        for char in strs:
            if char!=key:
                ans+=(str(num)+key) if num else ''
                key=char
                num=1
            else:
                num+=1
        ans+=(str(num)+key)
        return ans
    def countAndSay(self, n):
        ans='1'
        for _ in range(n-1):
            ans=self.generate(ans)
        return ans

a=Solution()
print(a.countAndSay(1))
print(a.countAndSay(2))
print(a.countAndSay(3))
print(a.countAndSay(4))
print(a.countAndSay(5))