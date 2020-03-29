
# 思路: 设定三个index: i,j,k扫描数组找到连续上升或者连续下降的个数

class Solution:
    def numTeams(self, rating):
        n=len(rating)
        ans=0
        for i in range(n-2):
            for j in range(i+1,n-1):
                x,y=rating[i],rating[j]
                for k in range(j+1,n):
                    if x<y<rating[k] or x>y>rating[k]:
                        ans+=1
        return ans

a=Solution()
print(a.numTeams([2,5,3,4,1]))
print(a.numTeams([1,2,3,4]))