# Input: arr = [4,2,1,3]
# Output: [[1,2],[2,3],[3,4]]
# Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.

# 思路: 将数组排序，从前往后寻找mindiff，并更新ans

class Solution:
    def minimumAbsDifference(self, arr):
        arr.sort()
        mindiff=float('inf')
        ans=[]
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i]<=mindiff:
                if arr[i+1]-arr[i]<mindiff:
                    ans=[[arr[i],arr[i+1]]]
                    mindiff=arr[i+1]-arr[i]
                else:
                    ans.append([arr[i],arr[i+1]])
        return ans

a=Solution()
print(a.minimumAbsDifference([3,8,-10,23,19,-4,-14,27]))