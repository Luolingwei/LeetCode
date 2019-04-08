import collections
class Solution:
    def canFinish(self, numCourses, prerequisites):
        restrict,course_conn=collections.defaultdict(set),collections.defaultdict(set)
        for tuple in prerequisites:
            restrict[tuple[0]].add(tuple[1])
            course_conn[tuple[1]].add(tuple[0])
        stack=[i for i in range(numCourses) if not restrict[i]]
        while stack:
            course=stack.pop()
            for i in course_conn[course]:
                restrict[i].remove(course)
                if not restrict[i]:
                    stack.append(i)
            restrict.pop(course)
        return not restrict

a=Solution()
print(a.canFinish(2,[[1,0]]))
print(a.canFinish(2,[[1,0],[0,1]]))
print(a.canFinish(5,[[1,0],[2,0],[3,1],[4,1],[5,3]]))
print(a.canFinish(3,[[1,0],[1,2],[0,1]]))