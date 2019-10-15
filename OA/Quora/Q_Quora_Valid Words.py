import re
class Solution:
    def valid(self,S,letters):
        memo,ans=set(letters),0
        strs=re.split('[^a-z]+',S.lower())
        for word in strs:
            if all(c in memo for c in word):
                ans+=1
        return ans

a=Solution()
print(a.valid("Hello,my dear friend!",['h', 'e', 'l', 'o', 'm']))