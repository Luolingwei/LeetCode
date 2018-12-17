class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        index=0
        row_start = 0
        col_start = 0
        row_end = n - 1
        col_end = n - 1
        ans = [[0]*n for _ in range(n)]
        while row_start<=row_end and col_start<=col_end:
            #turn right
            for i in range(col_start,col_end+1):
                index+=1
                ans[row_start][i]=index
            row_start+=1

            #turn down
            for i in range(row_start,row_end+1):
                index+=1
                ans[i][col_end]=index
            col_end-=1

            if row_start<=row_end:
                #turn left
                for i in range(col_end,col_start-1,-1):
                    index += 1
                    ans[row_end][i]=index
                row_end-=1

            if col_start<=col_end:
                #turn up
                for i in range(row_end,row_start-1,-1):
                    index += 1
                    ans[i][col_start]=index
                col_start+=1

        return ans

a = Solution()
print(a.generateMatrix(4))