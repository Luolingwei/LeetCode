class Solution:
    def convertToTitle(self, n):
        ans=''
        dic=ord('A')
        while n>0:
            n,reminder=divmod(n-1,26)
            ans+=chr(dic+reminder)
        return ans[::-1]

a=Solution()
print(a.convertToTitle(701))
print(a.convertToTitle(28))