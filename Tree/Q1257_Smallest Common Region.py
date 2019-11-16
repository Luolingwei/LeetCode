
# 思路: 寻找region1和region2的lowest common ancester，先构建children和parents的关系图，对region1向上search，找到其所有的parent chain
# 然后对region2向上search，一旦出现在region1的parent chain中，即为lowest common ancester.

class Solution:
    def findSmallestRegion(self, regions, region1, region2):
        dic={}
        for r in regions:
            for child in r[1:]:
                dic[child]=r[0]
        memo1={region1}
        while region1 in dic:
            region1=dic[region1]
            memo1.add(region1)
        while region2 not in memo1:
            region2=dic[region2]
        return region2

a=Solution()
print(a.findSmallestRegion([["Earth","North America","South America"],
["North America","United States","Canada"],
["United States","New York","Boston"],
["Canada","Ontario","Quebec"],
["South America","Brazil"]],"Quebec","New York"))