
# 思路: 将数组以第一个元素排序，Tail记录现在能cover的范围（不需要新拿数组进来），curMax记录目前能达到的范围，如果start大于curMax则范围已断.

class Solution:
    def videoStitching(self, clips, T):
        Tail, curMax, ans = -1, 0, 0
        for start, end in sorted(clips):
            if curMax>=T or start>curMax:
                break
            elif start>Tail:
                Tail,ans=curMax,ans+1
            curMax=max(curMax,end)
        return ans if curMax>=T else -1

a=Solution()
print(a.videoStitching([[0,2],[2,6],[8,10],[1,9],[1,5],[5,9]],10))
print(a.videoStitching([[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]],9))
print(a.videoStitching([[0,1],[1,2]],5))
print(a.videoStitching([[0,4],[2,8]],5))
print(a.videoStitching([[0,7]],7))
print(a.videoStitching([[0,0],[9,9],[2,10],[0,3],[0,5],[3,4],[6,10],[1,2],[4,7],[5,6]],5))
print(a.videoStitching([[0,1],[0,3],[2,4]],4))