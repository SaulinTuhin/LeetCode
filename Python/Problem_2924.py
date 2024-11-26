from typing import List

# Problem - 2924. Find Champion II
# Python3 Solution!
class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        champion_candidates = [True] * n
        
        for u, v in edges:
            champion_candidates[v] = False
        
        champion = -1
        champion_count = 0
        for i in range(n):
            if champion_candidates[i]:
                champion = i
                champion_count += 1
        
        return -1 if champion_count > 1 else champion
        
    
    def findChampion_1(self, n: int, edges: List[List[int]]) -> int:
        champion_set = {i for i in range(n)}
        
        for u, v in edges:
            if v in champion_set:
                champion_set.remove(v)
        
        return -1 if len(champion_set) > 1 else list(champion_set)[0]


if __name__=="__main__":
    sol = Solution()
    
    print(sol.findChampion(3, [[0,1],[1,2]]))
    print(sol.findChampion(4, [[0,2],[1,3],[1,2]]))