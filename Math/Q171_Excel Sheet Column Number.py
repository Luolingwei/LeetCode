class Solution:
    def titleToNumber(self, s):
        dic,ans,index=ord('A')-1,0,0
        for char in s[::-1]:
            ans+=(ord(char)-dic)*pow(26,index)
            index+=1
        return ans

a=Solution()
print(a.titleToNumber("ZY"))
print(a.titleToNumber("AB"))
print(a.titleToNumber("A"))
