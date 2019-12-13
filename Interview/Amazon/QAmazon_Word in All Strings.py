class Solution:
    def find(self,words,strs):
        res=[]
        for w in words:
            if all(w in s for s in strs):
                res.append(w)
        return res



a=Solution()
print(a.find(["ab","ac"],['abc','abf','abj']))