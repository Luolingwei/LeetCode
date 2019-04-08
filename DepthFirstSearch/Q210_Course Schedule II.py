import collections
class Solution:
    def findOrder(self, numCourses, prerequisites):
        restrict,course_conn=collections.defaultdict(set),collections.defaultdict(set)
        ans=[]
        for tuple in prerequisites:
            restrict[tuple[0]].add(tuple[1])
            course_conn[tuple[1]].add(tuple[0])
        stack=[i for i in range(numCourses) if not restrict[i]]
        while stack:
            course=stack.pop()
            ans.append(course)
            for i in course_conn[course]:
                restrict[i].remove(course)
                if not restrict[i]:
                    stack.append(i)
            restrict.pop(course)
        return ans if not restrict else []

a=Solution()
print(a.findOrder(2,[[0,1]]))
print(a.findOrder(2,[[1,0]]))
print(a.findOrder(2,[[1,0],[0,1]]))
print(a.findOrder(5,[[1,0],[2,0],[3,1],[4,1],[5,3]]))
print(a.findOrder(3,[[1,0],[1,2],[0,1]]))