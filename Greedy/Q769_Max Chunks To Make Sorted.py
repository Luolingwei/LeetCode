# Input: arr = [4,3,2,1,0]
# Output: 1
# Explanation:
# Splitting into two or more chunks will not return the required result.
# For example, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1, 2], which isn't sorted.

# Input: arr = [1,0,2,3,4]
# Output: 4
# Explanation:
# We can split into two chunks, such as [1, 0], [2, 3, 4].
# However, splitting into [1, 0], [2], [3], [4] is the highest number of chunks possible.

# 思路:  Greedy, 从左到右扫描，更新最大范围curMax，当i>curMax时，进入下一个chunk.
# 注意数组是0到len-1的数字，故数字就是排序后的index

class Solution:
    def maxChunksToSorted(self, arr):
        curMax,ans=-1,0
        for i,n in enumerate(arr):
            if i>curMax:
                ans+=1
            curMax=max(n,curMax)
        return ans

a=Solution()
print(a.maxChunksToSorted([4,3,2,1,0]))
print(a.maxChunksToSorted([1,0,2,3,4]))