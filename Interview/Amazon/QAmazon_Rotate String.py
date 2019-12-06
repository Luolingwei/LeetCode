class Solution:
    def rotate(self,strs):
        memo=set()
        ans=set()
        for s in strs:
            if s[1:]+s[0] in memo:
                ans.add((s,s[1:]+s[0]))
            elif s[-1]+s[:-1] in memo:
                ans.add((s,s[-1]+s[:-1]))
            else:
                memo.add(s)
        return ans

a=Solution()
print(a.rotate(["12","21","123","312","231","321","112"]))