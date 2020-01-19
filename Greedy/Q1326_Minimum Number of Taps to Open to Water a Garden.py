
# 思路1: 将所有喷泉转为interval存储，左边界取max(0,l)，按left排序，left相同的，取最大的right
# 从第0个开始，对于当前end范围内的left，拿最大的right进行范围扩展，(所有范围都要cover，所以下一个的left一定在当前end内)
# 结束条件为end到达末尾，在循环中如果某轮end无法再被扩展(curmax<=end)，直接break

# 思路2: dp, dp[i]表示cover i之前范围需要开的喷泉个数，对于每个喷泉(i,r)，其cover的范围是i-r到i+r
# 对于i-r到i+r的j, dp[j]=min(dp[j],dp[i-r]+1)表示开启当前喷泉，并更新此范围内的所有dp[i]

class Solution:
    def minTaps(self, n, ranges):
        intervals=[]
        for i,r in enumerate(ranges):
            intervals.append([max(0, i-r), i+r])
        intervals.sort(key=lambda x: (x[0],-x[1]))
        ans,cur,end=1,0,intervals[0][1]
        while end<n:
            curmax=0
            while cur<n+1 and intervals[cur][0]<=end:
                curmax=max(curmax,intervals[cur][1])
                cur+=1
            if curmax<=end: break
            end=curmax
            ans+=1
        return ans if end>=n else -1


    # def minTaps(self, n: int, ranges: List[int]) -> int:
    #     dp = [0] + [float('inf')] * n
    #     for i, r in enumerate(ranges):
    #         for j in range(max(0, i - r), min(n, i + r) + 1):
    #             dp[j] = min(dp[j], dp[max(0, i - r)] + 1)
    #     return dp[n] if dp[n] != float("inf") else -1


a=Solution()
print(a.minTaps(5,[3,4,1,1,0,0]))
print(a.minTaps(3,[0,0,0,0]))
print(a.minTaps(7,[1,2,1,0,2,1,0,1]))
print(a.minTaps(8,[4,0,0,0,0,0,0,0,4]))
print(a.minTaps(8,[4,0,0,0,4,0,0,0,4]))