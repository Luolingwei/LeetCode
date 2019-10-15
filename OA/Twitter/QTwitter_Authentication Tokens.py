
# 建立HashTable，记录每个token的状态，更新状态到最后判断>=T的token数

import collections
class Solution:
    def execute(self,commands,expire):
        memo=collections.defaultdict(int)
        for c,id,T in commands:
            if c==0:
                memo[id]=T+expire
            else:
                if memo[id]>=T:
                    memo[id]=T+expire
        return len([i for i in memo.values() if i>=T])

a=Solution()
print(a.execute([[0,1,1],[0,2,2],[1,1,5],[1,2,7]],4))