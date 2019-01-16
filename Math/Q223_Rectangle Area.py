class Solution:
    def find_interval(self, A, C, E, G):
        if C<=E or G<=A:
            return 0
        list=[A,C,E,G]
        list.sort()
        return list[2]-list[1]

    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        total=(C-A)*(D-B)+(G-E)*(H-F)
        return total-self.find_interval(A,C,E,G)*self.find_interval(F,H,B,D)

a=Solution()
print(a.computeArea(-3,0,3,4,0,-1,9,2))



