
# 思路: 先统计单数字符的个数
# 如果大于1个则返回[]
# 如果等于1个, 则以此字符为中心进行扩展
# 如果等于0个, 则以空字符为中心进行扩展
# 每次加上memo中任意一个个数大于0的字符在两边(2个), 直到所有字符都用完, 加入res

from collections import Counter
class Solution:
    def generatePalindromes(self, s):
        memo = Counter(s)
        single, singlec = 0, None
        for c,v in memo.items():
            if v&1:
                singlec = c
                single += 1
        res,target = [""], len(s)
        if single>1: return []
        if single == 1:
            res = [singlec]
            memo[singlec]-=1
            target -= 1

        self.ans = []
        def dfs(memo,res,used):
            if used==target:
                self.ans+=res
            for c,v in memo.items():
                if v>0:
                    tempres = [c+word+c for word in res]
                    memo[c]-=2
                    dfs(memo,tempres,used+2)
                    memo[c]+=2
        dfs(memo,res,0)
        return self.ans


a=Solution()
print(a.generatePalindromes("aabb"))
print(a.generatePalindromes("abc"))