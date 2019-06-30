# Input: books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], shelf_width = 4
# Output: 6
# Explanation:
# The sum of the heights of the 3 shelves are 1 + 3 + 2 = 6.
# Notice that book number 2 does not have to be on the first shelf.

# 思路: dp[i]表示前i本书能形成的最小高度，注意书要按照原顺序排列.
# 每进来一本书，有两种选择:
# 1. 自己单独一层，dp[i]=dp[i-1]+h[i]
# 2. 放到前面的书中，dp[i]=min(dp[j]+max(h[j]~h[i])) j从i-1到0 (拿出j到i-1的书和当前的i组成一层)

class Solution:
    def minHeightShelves(self, books, shelf_width):
        dp=[0]*(len(books)+1)
        for i in range(len(books)):
            w,h=books[i][0],books[i][1]
            dp[i+1]=dp[i]+h
            for j in range(i-1,-1,-1):
                w+=books[j][0]
                h=max(h,books[j][1])
                if w>shelf_width: break
                dp[i+1]=min(dp[i+1],dp[j]+h)
        return dp[-1]

a=Solution()
print(a.minHeightShelves([[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]],4))
print(a.minHeightShelves([[1,7],[6,4],[10,7],[6,10],[8,10],[1,10],[10,7]],10))