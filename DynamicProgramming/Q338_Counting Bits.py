class Solution:
    def countBits(self, num):
        res=[0]
        while len(res)<num+1:
            res+=[i+1 for i in res]
        return res[:num+1]

a=Solution()
print(a.countBits(2))
print(a.countBits(5))