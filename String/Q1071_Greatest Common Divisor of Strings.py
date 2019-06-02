class Solution:
    def gcdOfStrings(self, str1, str2):
        l1,l2=len(str1),len(str2)
        str=str1 if l1<l2 else str2
        for l in range(min(l1,l2),0,-1):
            if l1%l==0 and l2%l==0:
                sub=str[:l]
                if sub*(l1//l)==str1 and sub*(l2//l)==str2:
                    return sub
        return ""

a=Solution()
print(a.gcdOfStrings("ABCABC","ABC"))
print(a.gcdOfStrings("ABABAB","ABAB"))
print(a.gcdOfStrings("LEET","CODE"))
print(a.gcdOfStrings("A","AA"))