import collections
class Solution:
    # solution1 dfs
    # def dfs(self,candidates,res,start,sum):
    #     if start==len(candidates):
    #         if sum==0:
    #             res[0]+=1
    #             return
    #         else:
    #             return
    #     for num in candidates[start]:
    #         self.dfs(candidates,res,start+1,sum+num)
    #
    # def fourSumCount(self, A, B, C, D):
    #     """
    #     :type A: List[int]
    #     :type B: List[int]
    #     :type C: List[int]
    #     :type D: List[int]
    #     :rtype: int
    #     """
    #     res=[0]
    #     candidates=[A,B,C,D]
    #     self.dfs(candidates,res,0,0)
    #     return res[0]

    # solution2
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        dic_AB=collections.Counter(a+b for a in A for b in B)
        return sum(dic_AB[-c-d] for c in C for d in D)

a=Solution()
print(a.fourSumCount([1,2],[-2,-1],[-1,2],[0,2]))