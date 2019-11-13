class Solution:
    # 有正有负O，用memo记录preS，相同preS只记录最左边的， (n^2)
    # def maxSubArrayLen(self, nums, k):
    #     memo={0:-1}
    #     curS,ans=0,0
    #     for i,n in enumerate(nums):
    #         curS+=n
    #         for preS,prei in memo.items():
    #             if curS-preS<=k:
    #                 ans=max(ans,i-prei)
    #         if curS not in memo:
    #             memo[curS]=i
    #     return ans

    # 都是正数，滑动窗口， O(n)
    def maxSubArrayLen(self, nums, k):
        l=0
        curS,ans=0,0
        for r,n in enumerate(nums):
            curS+=n
            if curS>k:
                ans=max(ans,r-l)
                while curS>k:
                    curS-=nums[l]
                    l+=1
        ans=max(ans,len(nums)-l)
        return ans


a=Solution()
print(a.maxSubArrayLen([1,2,3,4,5,6],3))
print(a.maxSubArrayLen([3,1,1,2,1,6],5))
print(a.maxSubArrayLen([1,2,3,4,5,6],100))
print(a.maxSubArrayLen([1],1))