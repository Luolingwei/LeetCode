
# 按照分数和id排序，取得第rank-1个的id

class Solution:
    def FindRank(self,performances,rank):
        score=[(sum(p),i) for i,p in enumerate(performances)]
        score.sort(key=lambda s:(-s[0],s[1]))
        return score[rank-1][1]

a=Solution()
print(a.FindRank([[79,89,15],[85,89,92],[71,96,88]],2))
print(a.FindRank([[2,2,2],[2,2,2],[1,1,1]],2))