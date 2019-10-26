
# 思路: Two Pointers, 排序时带上index信息在后面，寻找小于等于target的最大数

class Solution:
    def find(self,movies,d):
        target=d-30
        movies=sorted((t,i) for i,t in enumerate(movies))
        l,r=0,len(movies)-1
        ans,maxT=[],0
        while l<r:
            curT=movies[l][0]+movies[r][0]
            if curT>target:
                r-=1
            else:
                if curT==target:
                    return [movies[l][1],movies[r][1]]
                elif curT>maxT:
                    maxT=curT
                    ans=[movies[l][1],movies[r][1]]
                l+=1
        return ans

a=Solution()
print(a.find([90, 85, 75, 60, 120, 150, 125],300))
print(a.find([90, 85, 75, 110, 120, 150, 160],300))
print(a.find([],300))