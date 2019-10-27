
# 思路1: dp, 对于每个无重复字母的word，将其与dic中不重复的words组合，并加入dp中，最后返回所有可能组合的最长长度
# bit mask+dfs, 先将每个无重复字母的word转为bit存入memo, 相同mask存最长长度，然后dfs求无重复mask的最长组合

class Solution:
    # Solution 1 dp
    # def maxLength(self, arr: List[str]) -> int:
    #     dp=collections.defaultdict(int)
    #     dp[""]=0
    #     for word in arr:
    #         for word2 in list(dp.keys()):
    #             if len(word)!=len(set(word)): break
    #             if len(set(word+word2))==len(word)+len(word2):
    #                 dp[word+word2]=max(dp[word+word2],len(word)+len(word2))
    #     return max(dp.values())

    # Solution 2 bit mask + dfs
    def maxLength(self, words) -> int:
        memo={}
        for word in words:
            if len(set(word))!=len(word):
                continue
            mask=0
            for c in word:
                mask|=1<<(ord(c)-97)
            memo[mask]=max(memo.get(mask,0),len(word))
        masks=list(memo.keys())
        N=len(masks)
        self.ans=0
        def dfs(curM,curC,start):
            self.ans=max(self.ans,curC)
            for i in range(start,N):
                if not curM&masks[i]:
                    dfs(curM|masks[i],curC+memo[masks[i]],i+1)
        dfs(0,0,0)
        return self.ans

a=Solution()
print(a.maxLength(["un","iq","ue"]))
print(a.maxLength(["cha","r","act","ers"]))
print(a.maxLength(["abcdefghijklmnopqrstuvwxyz"]))
print(a.maxLength(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p"]))
print(a.maxLength(["yy","bkhwmpbiisbldzknpm"]))