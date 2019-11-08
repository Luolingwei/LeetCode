
# 思路: 每个格子能存的water取决于左右的max，curW=min(lmax,rmax)-curH，如果对每个index扫左右求max, O(n^2)
# 可以用两个index l,r 相对走，动态更新lmax,rmax，对左边的lmax可以记录，但rmax无法更新，对右边的rmax可以记录，但lmax无法更新
# 解决方法: 每次移动左右更小的index，这样最终停在整个数组的最大值，对于左边rmax一定大于lmax，对于右边lmax一定大于rmax，所以无需更新

class Solution:
    # O(n^2)
    # def trap(self, height):
    #     N,ans=len(height),0
    #     for i in range(N):
    #         maxl,maxr=0,0
    #         for l in range(i):
    #             maxl=max(maxl,height[l])
    #         for r in range(i+1,N):
    #             maxr=max(maxr,height[r])
    #         ans+=max(min(maxl,maxr)-height[i],0)
    #     return ans

    # O(n)
    def trap(self, height):
        N,ans=len(height),0
        l,r=0,N-1
        lmax,rmax=0,0
        while l<r:
            if height[l]<height[r]:
                lmax=max(height[l],lmax)
                ans+=lmax-height[l]
                l+=1
            else:
                rmax=max(height[r],rmax)
                ans+=rmax-height[r]
                r-=1
        return ans

a = Solution()
print(a.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(a.trap([0,1,0,1,0,2,0,1,0,1,0]))
print(a.trap([5,4,1,2]))