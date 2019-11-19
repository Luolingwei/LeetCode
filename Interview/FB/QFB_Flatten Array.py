class Solution:
    def flatten(self,array):
        if not array: return []
        ans=[]
        for n in array:
            if isinstance(n,int):
                ans.append(n)
            else:
                ans+=self.flatten(n)
        return ans

a=Solution()
print(a.flatten([1,2,3,[4,5,[6]]]))
print(a.flatten([1,[6],2,[],3,[4,5,[[6]]]]))