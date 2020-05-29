from collections import defaultdict

# 思路: 先将各个word的index提取出来存储在list中
# 最短距离即两个word index数组的最小差值
# 因为两个数组都是递增, 一直缩小index1[i]和index2[j]的距离即可
# O(m+n)

class WordDistance:

    def __init__(self, words):
        self.index = defaultdict(list)
        for i, word in enumerate(words):
            self.index[word].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        index1, index2 = self.index[word1], self.index[word2]
        i, j = 0, 0
        res = float('inf')
        while i < len(index1) and j < len(index2):
            res = min(res, abs(index1[i] - index2[j]))
            if index1[i] < index2[j]:
                i += 1
            else:
                j += 1
        return res


a=WordDistance(["practice","makes","perfect","coding","makes"])
print(a.shortest("coding","practice"))
print(a.shortest("makes","coding"))
