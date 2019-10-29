
# 思路: 固定左边的i，在右边数组寻找小于target-nums[i]的组合
# 因为是排序后的数组，在右边寻找只需要固定l,r从尾部往前，这样l,r相对走，只走一遍，O(n)

class Solution:
    # O(n^2)
    def threeSumSmaller(self, nums, target):
        nums.sort()
        N,ans=len(nums),0
        for i in range(N-2):
            curT=target-nums[i]
            l,r=i+1,N-1
            while l<r:
                curS=nums[l]+nums[r]
                if curS<curT:
                    ans+=r-l
                    l+=1
                else:
                    r-=1
        return ans

a=Solution()
print(a.threeSumSmaller([3,1,0,-2],4))