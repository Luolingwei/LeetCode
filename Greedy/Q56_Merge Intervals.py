class Solution(object):
    """
    :type intervals: List[Interval]
    :rtype: List[Interval]
    """
    def merge(self, intervals):
        intervals.sort(key=lambda x:x[0])
        merged=[]
        for x in intervals:
            if not merged or x[0]>merged[-1][-1]:
                merged.append(x)
            else:
                merged[-1][-1]=max(merged[-1][-1],x[1])
        return merged

a=Solution()
print(a.merge([[1,3],[2,6],[8,10],[15,18]]))
print(a.merge([[1,4],[4,5]]))
print(a.merge([]))