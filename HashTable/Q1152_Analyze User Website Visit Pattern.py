from collections import Counter
from collections import defaultdict
from itertools import combinations

# 思路: 对所有log按time排序，根据user提取出每个user按时间顺序的访问记录
# 对每个user的访问记录集合取combinations，去重并计数
# 取Counter中出现次数最多的组合，如果相同取key小的

class Solution:
    def mostVisitedPattern(self, username, timestamp, website):
        c=Counter()
        by_user=defaultdict(list)
        for t,user,web in sorted(zip(timestamp,username,website)):
            by_user[user].append(web)
        for com in by_user.values():
            c+=Counter(set(combinations(com,3)))
        return min(c.keys(),key=lambda x:(-c[x],x))

a=Solution()
print(a.mostVisitedPattern(["joe","joe","joe","james","james","james","james","mary","mary","mary"],
                           [1,2,3,4,5,6,7,8,9,10],
                           ["home","about","career","home","cart","maps","home","home","about","career"]))