class Solution:
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        ans=0
        for p1 in points:
            map={}
            for p2 in points:
                dt=(p1[0]-p2[0])**2+(p1[1]-p2[1])**2
                map[dt]=map.get(dt,0)+1
            for dt in map:
                ans+=map[dt]*(map[dt]-1)
        return ans

a=Solution()
print(a.numberOfBoomerangs([[0,0],[1,0],[2,0]]))
