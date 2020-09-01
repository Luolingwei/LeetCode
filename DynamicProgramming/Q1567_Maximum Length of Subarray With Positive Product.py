
# 思路: pos, neg分别表示以当前数字结尾的正数, 负数最长序列长度
# 根据n的正负动态更新pos,neg, 找到最长的pos即可

class Solution:
    def getMaxLen(self, nums):
        pos, neg = 0, 0
        res = 0
        for n in nums:
            if n==0:
                neg, pos = 0, 0
            elif n>0:
                if neg>0: neg, pos = neg+1, pos+1
                else: neg, pos = 0, pos+1
            else:
                if neg>0: pos, neg = neg+1, pos+1
                else: neg, pos = pos+1, 0
            res = max(res,pos)
        return res


a=Solution()
print(a.getMaxLen([1,-2,-3,4]))
print(a.getMaxLen([0,1,-2,-3,-4]))