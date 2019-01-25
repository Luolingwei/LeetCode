import collections
class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        task=collections.Counter(tasks)
        task=sorted(task.values(),reverse=True)
        Gap_num=task[0]-1
        idles=Gap_num*n
        for num in task[1:]:
            idles-=min(num,Gap_num)
        return idles+sum(task) if idles>0 else sum(task)

a=Solution()
print(a.leastInterval(["A","A","A","B","B","B"],2))