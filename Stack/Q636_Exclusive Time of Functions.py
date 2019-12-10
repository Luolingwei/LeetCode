
class Solution:
    '''
    when we come across start, the time belongs to previous node
    when we come across end, the time belongs to current node
    '''
    def exclusiveTime(self, n, logs):
        time=[0]*n
        stack=[]
        pretime=0
        for s in logs:
            curnode,curstatus,curtime=s.split(':')
            curtime=int(curtime)
            if curstatus=='start':
                if stack:
                    time[stack[-1]]+=curtime-pretime
                stack.append(int(curnode))
                pretime=curtime
            else:
                time[stack.pop()]+=curtime-pretime+1
                pretime=curtime+1
        return time