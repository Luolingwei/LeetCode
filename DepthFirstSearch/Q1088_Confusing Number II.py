
# 思路: dfs搜索，每次加一位valid number，track它的rotation，比较n和rn是否相等

class Solution:
    def confusingNumberII(self, N):
        valid=[0,1,6,8,9]
        flip={0:0,1:1,6:9,8:8,9:6}
        self.ans=0
        def dfs(n,rn,digit):
            if n!=rn:
                self.ans+=1
            for i in valid:
                if n==0 and i==0:
                    continue
                if n*10+i<=N:
                    dfs(n*10+i,flip[i]*digit+rn,digit*10)
        dfs(0,0,1)
        return self.ans

a=Solution()
print(a.confusingNumberII(20))