# Input:
# [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
#
# Output:
# [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

# 思路:将hight按照从大到小排序，那么就可以借鉴dp的思路，每新来一个tuple，比它大（或等于）的元素都已经在ans中，所以它后面的位置index就是其插入ans的位置，依次添加所有tuple即可
# 需要注意的是如果height相同那么按照index从小到大排序，因为index越小，在原队列中越靠前，相当于越大

class Solution:
    def reconstructQueue(self, people):
        ans=[]
        queue=sorted(people,key=lambda x:(-x[0],x[1]))
        for pair in queue:
            ans.insert(pair[1],pair)
        return ans

a=Solution()
print(a.reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]))