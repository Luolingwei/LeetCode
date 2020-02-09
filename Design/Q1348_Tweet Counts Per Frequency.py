from collections import defaultdict
import bisect

# 思路: 用list存储时间序列，用bisect搜索每个interval之间的记录个数

class TweetCounts:

    def __init__(self):
        self.memo = defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        bisect.insort(self.memo[tweetName],time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int):
        gap = 60 if freq == 'minute' else 3600 if freq == 'hour' else 86400
        i = startTime
        res = []
        while i <= endTime:
            j = min(i + gap, endTime+1)
            res.append(bisect.bisect_left(self.memo[tweetName], j) - bisect.bisect_left(self.memo[tweetName], i))
            i += gap
        return res


# Your TweetCounts object will be instantiated and called as such:
obj = TweetCounts()
obj.recordTweet("tweet3",0)
obj.recordTweet("tweet3",60)
obj.recordTweet("tweet3",10)
print(obj.getTweetCountsPerFrequency("minute","tweet3",0,59))
print(obj.getTweetCountsPerFrequency("minute","tweet3",0,60))
obj.recordTweet("tweet3",120)
print(obj.getTweetCountsPerFrequency("hour","tweet3",0,210))