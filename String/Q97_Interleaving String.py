class Solution:
    def isInterleave(self, s1, s2, s3):
        def helper(i, j, visited):
            if i+j==l3:
                return True
            if i<l1 and s1[i]==s3[i+j] and (i+1,j) not in visited:
                visited.add((i+1,j))
                if helper(i+1,j,visited):
                    return True
            if j<l2 and s2[j]==s3[i+j] and (i,j+1) not in visited:
                visited.add((i,j+1))
                if helper(i,j+1,visited):
                    return True
            return False
        l1=len(s1);l2=len(s2);l3=len(s3)
        if l1+l2!=l3: return False
        return helper(0,0,set())

a=Solution()
print(a.isInterleave("aabcc","dbbca","aadbbcbcac"))
print(a.isInterleave("aabcc","dbbca","aadbbbaccc"))