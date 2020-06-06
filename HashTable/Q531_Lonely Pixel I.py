from collections import Counter

# 思路1: 先遍历一遍记录所有行和列包含的B的个数, 再次遍历找出像素为B且当前行只有1个当前列只有1个的(i,j)
# 优化: 只找rows[i]==1的行, 因为这里只有一个B, 找到这个B之后检查cols[j]是否等于1

class Solution:
    # def findLonelyPixel(self, picture):
    #     rows = Counter()
    #     cols = Counter()
    #     m, n = len(picture), len(picture[0])
    #     for i in range(m):
    #         for j in range(n):
    #             if picture[i][j] == "B":
    #                 rows[i] += 1
    #                 cols[j] += 1
    #     return sum([picture[i][j] == "B" and rows[i] == 1 and cols[j] == 1 for i in range(m) for j in range(n)])

    def findLonelyPixel(self, picture):
        rows = Counter()
        cols = Counter()
        m,n,res = len(picture), len(picture[0]),0
        for i in range(m):
            for j in range(n):
                if picture[i][j] == "B":
                    rows[i]+=1
                    cols[j]+=1
        for i in range(m):
            if rows[i]!=1:
                continue
            for j in range(n):
                if picture[i][j] == "B":
                    res += (cols[j]==1)
                    break
        return res


a=Solution()
print(a.findLonelyPixel([['W', 'W', 'B'],['W', 'B', 'W'],['B', 'W', 'W']]))