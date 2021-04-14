
# 思路1: 每次随机选择一个word, 得到score, 留下list中和当前guess match结果为score的word

# 思路2: 因为最有可能的情况是一个字符都不match, 概率为 (25/26)^6 = 80%, 所以最有可能的情况是首先guess到match score=0,
# 可以从candidates中选择和其他word的 match score = 0 数量最小的word, 这样candidates 集合减小最快
# O(N^2)

# 思路3: 根据char frequency的总和 选择family 最大的那个word, 这样一旦guess到match score=0, 所有和这个word有重叠的candidate都会被剔除掉
# 理论上guess所有位置freq最大char组成的word, 可以一次剔除最多的candidate, 但是本题只能在wordlist中guess
# O(N)

# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

import random
from collections import Counter
class Solution:

    def findSecretWord1(self, wordlist, master):
        def match(x, y):
            return sum(x[i] == y[i] for i in range(len(x)))

        for _ in range(10):
            word = random.choice(wordlist)
            score = master.guess(word)
            wordlist = [w for w in wordlist if match(w, word) == score]


    def findSecretWord2(self, wordlist, master):
        def match(x, y):
            return sum(x[i] == y[i] for i in range(len(x)))

        def select(wordlist):
            count = Counter()
            for i in range(len(wordlist)):
                for j in range(len(wordlist)):
                    if j != i and match(wordlist[i], wordlist[j]) == 0:
                        count[i] += 1
            return min(range(len(wordlist)), key=lambda x: count[x])

        for _ in range(10):
            word = wordlist[select(wordlist)]
            score = master.guess(word)
            wordlist = [w for w in wordlist if match(w, word) == score]


    def findSecretWord3(self, wordlist, master) -> None:
        def match(x, y):
            return sum(x[i] == y[i] for i in range(len(x)))

        def select(wordlist):
            freqs = [Counter(w[i] for w in wordlist) for i in range(6)]
            word = max(wordlist, key=lambda x: sum(freqs[i][c] for i, c in enumerate(x)))
            return word

        for _ in range(10):
            word = select(wordlist)
            score = master.guess(word)
            wordlist = [w for w in wordlist if match(w, word) == score]