
# 思路: 按每一位进行计算，用mask进行掩膜，每一位上的total Hamming distant 等于0的个数乘以1的个数.累加起来即可

class Solution:
    def totalHammingDistance(self, nums):
        ans,mask=0,1
        for i in range(32):
            ones,zeros=0,0
            for num in nums:
                if mask&num: ones+=1
                else: zeros+=1
            ans+=ones*zeros
            mask<<=1
        return ans

a=Solution()
print(a.totalHammingDistance([4, 14, 2]))