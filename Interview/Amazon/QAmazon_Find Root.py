class Solution:
    def find(self,array):
        degree=set()
        candidates=[]
        for pair in array:
            candidates.append(pair[0])
            for child in pair[1:]:
                degree.add(child)
        for node in candidates:
            if node not in degree:
                return node
        return -1

a=Solution()
print(a.find([[5,7,8],[7,1,2],[8,10,3],[4,5]]))