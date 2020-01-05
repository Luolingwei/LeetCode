
# 思路: 建立索引的集合，随机pop一个word，计算curscore，剩下的words与当前word的score等于curscore才可能是secret.
# 首先对wordlist进行随机化，用首字母排序

# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, wordlist, master):
        def myguess(word, match):
            ans = 0
            for i in range(6):
                if word[i] == match[i]:
                    ans += 1
            return ans

        wordlist.sort(key=lambda x: x[0])
        wordsets = set(range(len(wordlist)))
        while wordsets:
            curi = wordsets.pop()
            score = master.guess(wordlist[curi])
            wordsets = {i for i in wordsets if myguess(wordlist[i], wordlist[curi]) == score}