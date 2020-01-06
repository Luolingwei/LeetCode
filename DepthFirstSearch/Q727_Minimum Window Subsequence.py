
# 思路: 此题要求有序匹配，从前往后搜索，碰到T[0]时往后搜索T剩下的元素，如果哪次没搜到(-1)，返回inf，全部找到时(j=n)返回i的位置

class Solution:
    def minWindow(self, S: str, T: str) -> str:
        ans,L="",float('inf')
        m,n=len(S),len(T)
        def dfs(i,j):
            if j==n: return i
            idx=S.find(T[j],i)
            if idx==-1:
                return float('inf')
            else:
                return dfs(idx+1,j+1)
        for start,c in enumerate(S):
            if c==T[0]:
                end=dfs(start,0)
                if end-start<L:
                    L=end-start
                    ans=S[start:end]
        return ans

a=Solution()
print(a.minWindow("abcdebdde","bde"))