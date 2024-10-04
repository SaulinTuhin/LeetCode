from typing import List, DefaultDict

# Problem - 2491. Divide Players Into Teams of Equal Skill
# Python3 Solution!
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        if n == 2:
            return skill[0] * skill[1]
        skill_map = DefaultDict(int)
        total = 0
        for num in skill:
            skill_map[num] += 1
            total += num
        if total % (n//2) != 0:
            return -1
        
        team_skill = total // (n // 2)
        chemistry = 0
        for num in skill:
            if skill_map[num] < 1:
                continue
            skill_map[num] -= 1
            if skill_map[team_skill - num] > 0:
                chemistry += (num * (team_skill - num))
                skill_map[team_skill - num] -= 1
            else:
                return -1
        return chemistry


if __name__=="__main__":
    sol = Solution()

    print(sol.dividePlayers([5,3,7,1]))
    print(sol.dividePlayers([3,2,5,1,3,4]))
    print(sol.dividePlayers([3,4]))
    print(sol.dividePlayers([1,1,2,3]))