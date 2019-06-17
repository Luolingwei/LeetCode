# Input: values = [5,4,3,2,1], labels = [1,1,2,2,3], num_wanted = 3, use_limit = 1
# Output: 9
# Explanation: The subset chosen is the first, third, and fifth item.

# 思路: 按value从大到小排序，并依次选择，如果某label已经到了limit，则往后挑选.直到选够num_wanted.

import collections
class Solution:
    def largestValsFromLabels(self, values, labels, num_wanted, use_limit):
        pairs=sorted(zip(values,labels),reverse=True)
        dic_label,ans=collections.defaultdict(int),0
        for value, label in pairs:
            if num_wanted:
                if dic_label[label]<use_limit:
                    ans+=value
                    dic_label[label]+=1
                    num_wanted-=1
            else:break
        return ans

a=Solution()
print(a.largestValsFromLabels([5,4,3,2,1],[1,1,2,2,3],3,1))
print(a.largestValsFromLabels([5,4,3,2,1],[1,3,3,3,2],3,2))
print(a.largestValsFromLabels([9,8,8,7,6],[0,0,0,1,1],3,1))
print(a.largestValsFromLabels([9,8,8,7,6],[0,0,0,1,1],3,2))