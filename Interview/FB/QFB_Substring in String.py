class Solution:
    # window
    # def find(self,subS,s):
    #     ans=0
    #     subL,sL=len(subS),len(s)
    #     l,r=0,subL
    #     window=s[l:r]
    #     while r<=sL:
    #         if window==subS:
    #             ans+=1
    #         if r==sL: break
    #         window=window[1:]
    #         window+=s[r]
    #         r+=1
    #         l+=1
    #     return ans

    # without window
    def find(self,subS,s):
        ans=0
        subL,sL=len(subS),len(s)
        l,r=0,subL
        while r<=sL:
            if s[l:r]==subS:
                ans+=1
            r+=1
            l+=1
        return ans

a=Solution()
print(a.find('aaacabba','aa'))
print(a.find('aa','aaacabba'))
print(a.find('a','aaacabba'))
print(a.find('aaa','aaacabba'))
print(a.find('ca','aaacabba'))