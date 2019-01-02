# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if len(points)<=2:
            return len(points)
        result=0
        for i in range(len(points)):
            dic={}
            overlap=0
            for j in range(i+1,len(points)):
                dx, dy =points[j].x-points[i].x,points[j].y-points[i].y
                if dx==0 and dy==0:
                    overlap+=1
                    continue
                slope=10.0*dy/dx if dx!=0 else 'Inf'
                dic[slope]=dic.get(slope,0)+1
            if not dic.values():
                result=max(result,overlap+1)
            else:
                result = max(result,overlap+max(dic.values())+1)
        return result

