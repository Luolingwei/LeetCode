class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        h_index=0
        citations.sort(reverse=True)
        for i in range(len(citations)):
            if citations[i]>=i+1:
                h_index=max(h_index,i+1)
            else:
                break
        return h_index

a=Solution()
print(a.hIndex([3,0,6,1,5]))