
# 思路: 对words进行dfs，带上Counter和当前score作为参数，相当于遍历所有可行的组合，找出最大score

from collections import Counter
class Solution:
    def maxScoreWords(self, words, letters, score):
        self.ans = 0
        count = Counter(letters)
        word_score = {word: sum(score[ord(c) - 97] for c in word) for word in words}
        def dfs(words, count, curS):
            self.ans = max(self.ans, curS)
            for i in range(len(words)):
                cword = Counter(words[i])
                if all(count[c] >= cword[c] for c in cword):
                    dfs(words[i + 1:], count - cword, curS + word_score[words[i]])
        dfs(words, count, 0)
        return self.ans

a=Solution()
print(a.maxScoreWords(["dog","cat","dad","good"],["a","a","c","d","d","d","g","o","o"],[1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]))
print(a.maxScoreWords(["leetcode"],["l","e","t","c","o","d"],[0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]))