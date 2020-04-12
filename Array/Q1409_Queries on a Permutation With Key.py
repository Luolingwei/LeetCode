
# 思路: pos记录每次数字的位置
# 每次更新时，pos[q-1]为q的实际位置，位置比它小的pos+1，将其位置置为0

class Solution:
    def processQueries(self, queries, m):
        pos = [i for i in range(0, m)]
        ans = []
        for q in queries:
            curpos = pos[q - 1]
            ans.append(curpos)
            for i, p in enumerate(pos):
                if p < curpos:
                    pos[i] += 1
            pos[q - 1] = 0
        return ans
