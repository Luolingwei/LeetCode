
# 思路: 标准dfs, 每次给pattern[i]安排一定长度的word, 并用dic记录
# 如果碰到memo之前记录过的pattern[i], 那么word下面对应长度的word一定要是memo[pattern[i]]
# 如果碰到memo中未出现的pattern[i], 给它安排长度1-len(word)的word, 并且这个word不能在memo.value()中已存在
# 用used(set)表示memo的values, 优化一下, 存储所有已经用过的words

class Solution:
    def wordPatternMatch(self, pattern, word):
        def dfs(word, memo, i, used):
            if not word or i==len(pattern):
                return not word and i==len(pattern)
            if pattern[i] in memo:
                curword = memo[pattern[i]]
                if word[:len(curword)] == curword:
                    if dfs(word[len(curword):], memo, i+1, used):
                        return True
                return False
            else:
                for j in range(1,len(word)+1):
                    curword = word[:j]
                    if curword not in used:
                        memo[pattern[i]] = curword
                        used.add(curword)
                        if dfs(word[j:],memo,i+1,used):
                            return True
                        memo.pop(pattern[i])
                        used.remove(curword)
                return False
        return dfs(word,{},0,set())


a=Solution()
print(a.wordPatternMatch("abab","redblueredblue"))
print(a.wordPatternMatch("aaaa","asdasdasdasd"))
print(a.wordPatternMatch("aabb","xyzabcxzyabc"))