# Input: [3,1,5,8] ---> [1,3,1,5,8,1]
# Output: 167
# Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
#              coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167


# 思路: 以最后一个扎破的气球为分界线(视作水泥气球,即最后一个扎破)，每个数组的最大值=左边数组的最大值+右边数组的最大值+nums[left]*nums[i]*nums[right]，取最大值即可得到最优解
# 所以要bottom-up，从最小的数组的最大值算起，每次让数组的宽度加1，这样不管怎么分割子最优解都会存在，一直将数组的宽度扩大至n(gap=n-1)

# Note: dp[i][i+1]=0是因为两边视作水泥气球,中间没有气球可扎

class Solution:
    def maxCoins(self, nums):
        nums=[1]+nums+[1]
        n=len(nums)
        dp=[[0]*n for _ in range(n)]
        for gap in range(2,n):
            for left in range(n-gap):
                right=left+gap
                for i in range(left+1,right):
                    dp[left][right]=max(dp[left][right],dp[left][i]+dp[i][right]+nums[left]*nums[i]*nums[right]) #分界线i从left游走到right
        return dp[0][n-1]


a=Solution()
print(a.maxCoins([3,1,5,8]))