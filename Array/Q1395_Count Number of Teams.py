
# 思路1: 设定三个index: i,j,k扫描数组找到连续上升或者连续下降的个数
# 思路2: 设定中间的数字rating[i]，遍历左右的数字，记录左右比它大/小的数字个数。以当前为中间数字的组合个数为(ls*rl+ll*rs)

class Solution:
    # O(n^3)
    # def numTeams(self, rating):
    #     n=len(rating)
    #     ans=0
    #     for i in range(n-2):
    #         for j in range(i+1,n-1):
    #             x,y=rating[i],rating[j]
    #             for k in range(j+1,n):
    #                 if x<y<rating[k] or x>y>rating[k]:
    #                     ans+=1
    #     return ans

    # O(n^2)
    def numTeams(self, rating):
        n=len(rating)
        ans=0
        for i in range(n):
            curnum = rating[i]
            ll,ls,rl,rs=0,0,0,0
            for l in range(i):
                if rating[l]>curnum:
                    ll+=1
                else:
                    ls+=1
            for r in range(i+1,n):
                if rating[r]>curnum:
                    rl+=1
                else:
                    rs+=1
            ans+=(ls*rl+ll*rs)
        return ans

a=Solution()
print(a.numTeams([2,5,3,4,1]))
print(a.numTeams([1,2,3,4]))