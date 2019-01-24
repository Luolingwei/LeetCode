class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic={}
        for num in nums:
            dic[num]=dic.get(num,0)+1
        ans=sorted(dic.items(),key=lambda d:d[1],reverse=True)
        return [ans[i][0] for i in range(k)]

a=Solution()
print(a.topKFrequent([1,1,1,2,2,3],2))
print(a.topKFrequent([1,1,1],1))
print(a.topKFrequent([1],1))