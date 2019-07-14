# Input: req_skills = ["java","nodejs","reactjs"], people = [["java"],["nodejs"],["nodejs","reactjs"]]
# Output: [0,2]

# 用位运算符表示skill_set，最后返回dp[1<<len(skills)-1]
# 每来一个新的People，将他的技能与已有的组合进行融合，如果不在组合中，加入。如果在组合中而且已有的len+1<dp[skills]，更新dp[skills]

class Solution:
    def smallestSufficientTeam(self, req_skills, people):
        dic={skill:1<<i for i,skill in enumerate(req_skills)}
        dp={0:[]}
        for i,p in enumerate(people):
            his_skills=0
            for skill in p:
                his_skills|=dic[skill]
            for skill_set, need in list(dp.items()):
                curskills=skill_set|his_skills
                if curskills not in dp or len(need)+1<len(dp[curskills]):
                    dp[curskills]=need+[i]
        return dp[(1<<len(req_skills))-1]


a=Solution()
print(a.smallestSufficientTeam(["java","nodejs","reactjs"],[["java"],["nodejs"],["nodejs","reactjs"]]))