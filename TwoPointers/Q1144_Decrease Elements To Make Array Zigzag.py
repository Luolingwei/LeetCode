# Input: nums = [1,2,3]
# Output: 2
# Explanation: We can decrease 2 to 0 or 3 to 1.

# 思路: Zigzag的条件是每个奇数位或每个偶数位的数都比两边的数小
# 返回两种方法的最小moves

class Solution:
    def movesToMakeZigzag(self, nums):
        A=[float('inf')]+nums+[float('inf')]
        moves=[0,0]
        for i in range(1,len(A)-1):
            moves[i%2]+=max(0,A[i]-min(A[i-1],A[i+1])+1)
        return min(moves)

a=Solution()
print(a.movesToMakeZigzag([9,6,1,6,2]))
print(a.movesToMakeZigzag([1,2,3]))