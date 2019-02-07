class Solution:
    def leastBricks(self, wall):
        dic={}
        for line in wall:
            temp=0
            for num in line[:-1]:
                temp+=num
                dic[temp]=dic.get(temp,0)+1
        return len(wall) if not dic else len(wall)-max(dic.values())

a=Solution()
print(a.leastBricks([[1],
        [1],
        [1]]))
print(a.leastBricks([[1,2,2,1],
        [3,1,2],
        [1,3,2],
        [2,4],
        [3,1,2],
        [1,3,1,1]]))
