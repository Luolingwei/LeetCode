
# 思路: bfs每次shrink一个字符, 并判断是否在allowed list中

class Solution:
    def judge(self, wordDict, s):
        allowed = set(wordDict)
        bfs = {s}
        while bfs:
            new_bfs = set()
            for word in bfs:
                if len(word)>1:
                    for i in range(len(word)):
                        new_word = word[:i]+word[i+1:]
                        if new_word not in allowed: return False
                        new_bfs.add(new_word)
            bfs = new_bfs
        return True


a=Solution()
print(a.judge(["ab","ac","bc","a","b","c"],"abc"))
print(a.judge(["a","aa"],"aaa"))