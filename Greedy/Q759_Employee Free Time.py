
# 思路: 对所有interval按start排序，每来一个interval，如果start>curend，说明有空闲，加入inerval，更新curend

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        event=[i for sub in schedule for i in sub]
        event.sort(key=lambda x:x.start)
        curend=float('-inf')
        ans=[]
        for interval in event:
            if interval.start>curend:
                ans.append(Interval(curend,interval.start))
                curend=interval.end
            else:
                curend=max(interval.end,curend)
        return ans[1:]