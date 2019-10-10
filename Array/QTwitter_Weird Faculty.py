
# 思路: 扫一遍数组找到第一个符合条件的点即可

class Solution:
    def findmin(self,nums):
        L,S=len(nums),sum(nums)
        total=S-(L-S)
        if total<0: return 0
        myR,hisR=0,total
        for i,n in enumerate(nums):
            if n: myR,hisR=myR+1,hisR-1
            else: myR,hisR=myR-1,hisR+1
            if myR>hisR: return i+1
        return -1

a=Solution()
print(a.findmin([1, 0, 0, 1, 0]))
print(a.findmin([1, 0, 0, 1, 1]))
print(a.findmin([1, 1, 1, 0, 1]))