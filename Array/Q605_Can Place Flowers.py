class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count=0
        flowerbed.append(0)
        flowerbed.insert(0,0)
        for i in range(1,len(flowerbed)-1):
            if flowerbed[i-1]+flowerbed[i]+flowerbed[i+1]==0:
                count+=1
                flowerbed[i]=1
        return count>=n

a=Solution()
print(a.canPlaceFlowers([1],0))
print(a.canPlaceFlowers([1,0,0,0,1],1))
print(a.canPlaceFlowers([1,0,0,0,1],2))
print(a.canPlaceFlowers([0,1,0,0,0,0,0,1,0,],3))