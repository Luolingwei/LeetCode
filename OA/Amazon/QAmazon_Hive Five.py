
# 思路: 用dic存储每个id的scores，scores用Heap存，然后遍历dic，从heap中取出前5个

import collections
import heapq
class Solution:
    def highfive(self,results):
        dic,ans=collections.defaultdict(list),{}
        for id,score in results:
            heapq.heappush(dic[id],-score)
        for id in dic.keys():
            curS,count=0,0
            for _ in range(5):
                if dic[id]:
                    curS-=heapq.heappop(dic[id])
                    count+=1
                else:
                    break
            ans[id]=curS/count
        return ans

a=Solution()
print(a.highfive([[1,80],[2,67],[1,90],[2,65],[2,54],[1,34],[1,23],[1,90],[1,100]]))