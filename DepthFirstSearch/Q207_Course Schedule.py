import collections
class Solution:
    def canFinish(self, numCourses, prerequisites):
        restrict=collections.defaultdict(set)
        for pair in prerequisites:
            restrict[pair[0]].add(pair[1])
        i_dic=set([i for i in range(numCourses) if i not in restrict.keys()])
        while restrict:
            flag = 0
            for i in list(restrict.keys()):
                if restrict[i].issubset(i_dic):
                    i_dic.add(i)
                    restrict.pop(i)
                    flag = 1
            if flag == 0: break
        return not restrict


a=Solution()
print(a.canFinish(2,[[1,0]]))
print(a.canFinish(2,[[1,0],[0,1]]))
print(a.canFinish(5,[[1,0],[2,0],[3,1],[4,1],[5,3]]))
print(a.canFinish(3,[[1,0],[1,2],[0,1]]))