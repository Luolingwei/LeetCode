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