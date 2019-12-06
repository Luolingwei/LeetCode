from collections import Counter
class Solution:
    def maxfreq(self,orders):
        count=Counter()
        for order in orders:
            if order[0]=='+':
                count[order[1:]]+=1
        return min(count.keys(),key=lambda x:(-count[x],x))

a=Solution()
print(a.maxfreq(["+1A", "+3E", "-1A", "+4F", "+1A", "-3E"]))
print(a.maxfreq(["+1A", "+0B", "-1A", "+4F", "+1A", "+0B"]))
print(a.maxfreq(["+1A", "-1A", "+1B", "+1A", "-1B", "+1B"]))