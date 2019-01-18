class Solution:
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        #solution1
        # overlap,length=0,len(timeSeries)
        # for i in range(length-1):
        #     if timeSeries[i]+duration-1>=timeSeries[i+1]:
        #         overlap+=timeSeries[i]+duration-timeSeries[i+1]
        # return length*duration-overlap

        #solution2
        ans=len(timeSeries)*duration
        for i in range(1,len(timeSeries)):
            ans-=max(0,duration-(timeSeries[i]-timeSeries[i-1]))
        return ans

a=Solution()
print(a.findPoisonedDuration([1,2], 2))
print(a.findPoisonedDuration([1,4], 2))