
# 思路: i到j的xor=0到j的xor^0到i的xor
# x^a^a=x

class Solution:
    def xorQueries(self, arr, queries):
        ans=[]
        for i in range(1,len(arr)):
            arr[i]^=arr[i-1]
        for i,j in queries:
            ans.append(arr[j]^arr[i-1] if i>0 else arr[j])
        return ans