
# 思路: 用bit表示每个字母出现的奇偶次数
# 一共5位，每次异或操作, 1代表出现了奇数次, 0代表出现了偶数次
# bit一共有32种情况, 用dic记录出现每种bit最小的index
# 每次生成一个新的bit, 找到同样bit的之前index, 他们中间的就是最长的偶数string

class Solution:
    def findTheLongestSubstring(self, s):
        chars = {'a':0,'e':1,'i':2,'o':3,'u':4}
        memo = {0:-1}
        bit,res = 0,0
        for i,c in enumerate(s):
            if c in chars:
                bit^=1<<chars[c]
                memo.setdefault(bit,i)
            res = max(res,i-memo[bit])
        return res

a=Solution()
print(a.findTheLongestSubstring("eleetminicoworoep"))