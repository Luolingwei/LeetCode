
# 思路: 统计所有点中最左上和右下的坐标，然后判断左上右下构成的面积是否等于总面积，这是条件之一，第二个条件是判断corner是否是由最左上和右下的点构成的4个点
# 这里用到了set的^方法，即重复出现的元素消失，加入非重复元素，比单纯用dic统计方便很多.

class Solution:
    def isRectangleCover(self, rectangles):
        corner=set()
        a,b,c,d,area=float('inf'),float('inf'),float('-inf'),float('-inf'),0
        for x1,y1,x2,y2 in rectangles:
            if x1<=a and y1<=b: a,b=x1,y1
            if x2>=c and y2>=d: c,d=x2,y2
            area+=(x2-x1)*(y2-y1)
            corner^={(x1,y1),(x2,y2),(x1,y2),(x2,y1)}
        return corner=={(a,b),(c,d),(a,d),(c,b)} and area==(c-a)*(d-b)

a=Solution()
print(a.isRectangleCover([[1,1,3,3],
  [3,1,4,2],
  [3,2,4,4],
  [1,3,2,4],
  [2,3,3,4]]))

print(a.isRectangleCover([
  [1,1,2,3],
  [1,3,2,4],
  [3,1,4,2],
  [3,2,4,4]
]))

print(a.isRectangleCover([
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [2,2,4,4]
]))

print(a.isRectangleCover([
  [0,0,1,1],
  [0,1,3,2],
  [1,0,2,2]]))

print(a.isRectangleCover([
  [0,0,1,1],
  [0,0,2,1],
  [1,0,2,1],
  [0,2,2,3]]))