import heapq

# 核心思想: 从左到右扫描，记录所有的高度变化点
# 在L,R(可能产生高度变化的地方) 处计算当前的最高高度, 如果有变化，则记录

class Solution:
    def getSkyline(self, buildings):

        # 记录高度上升事件, 如果两个升高事件同时发生, 先处理高的那个(H大的), 则只会有一次高度变化, 否则会有两次
        events = [(L, -H, R) for L, R, H in buildings]

        # 记录高度下降事件，高度下降用来处理可能的高度变化，因为在R的位置会有高度失效, 多个R重合只需要1个
        events += list(set([(R, 0, 0) for _, R, _ in buildings]))

        # 对event按时间顺序排列
        events.sort()

        # 记录当前存活的高度, 并一同记录高度存活的时间
        heights = [(0, float('inf'))]

        # (时间, 高度)
        res = [[0, 0]]

        for t, H, R in events:

            # 升高事件, 将高度push到堆中, 并记录存活时间
            if H:
                heapq.heappush(heights, (H, R))

            # 清除当前时间已经失效的height
            while heights[0][1] <= t:
                heapq.heappop(heights)

            # 现在可以获取到当前时间的最高高度，如果相比之前有变化，则记录
            if -heights[0][0] != res[-1][1]:
                res.append([t, -heights[0][0]])

        return res[1:]

a=Solution()
print(a.getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]))