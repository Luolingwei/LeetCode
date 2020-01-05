
# 思路: 先bfs找出第level层的friend，注意用set因为可能有重复，最后用Counter统计并排序

import collections
class Solution:
    def watchedVideosByFriends(self, watchedVideos, friends, id, level):
        bfs,visited={id},{id}
        for _ in range(level):
            bfs={j for i in bfs for j in friends[i] if j not in visited}
            visited|=bfs
        freq=collections.Counter([v for idx in bfs for v in watchedVideos[idx]])
        return sorted(freq.keys(),key=lambda x:(freq[x],x))