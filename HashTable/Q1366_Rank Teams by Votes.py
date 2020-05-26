
# 思路1: 用数组记录每个字母得到每种排位的个数, 最后根据数组排序
# 思路2: 直接用dic记录每个字母的得分数组, 根据数组排序, 把字母本身添加到数组末尾, 可方便按字母排序

class Solution:
    # def rankTeams(self, votes):
    #     base = ord('A')
    #     rank = [[0]*26 for _ in range(26)]
    #     for v in votes:
    #         for i,c in enumerate(v):
    #             rank[ord(c)-base][i]+=1
    #     return ''.join(sorted(votes[0],key=lambda x: (rank[ord(x)-base],-ord(x)),reverse=True))

    def rankTeams(self, votes):
        rank = {c: [0] * len(votes[0]) + [c] for c in votes[0]}
        for v in votes:
            for i, c in enumerate(v):
                rank[c][i] -= 1
        return ''.join(sorted(votes[0], key=lambda c: (rank[c])))

a=Solution()
print(a.rankTeams(["ABC","ACB","ABC","ACB","ACB"]))
print(a.rankTeams(["ZMNAGUEDSJYLBOPHRQICWFXTVK"]))