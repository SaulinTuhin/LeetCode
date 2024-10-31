from typing import List

# Problem - 2463. Minimum Total Distance Traveled
# Python3 Solution!
class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        
        factory_flatten = []
        for f in factory:
            for i in range(f[1]):
                factory_flatten.append(f[0])
                
        ROBOT, FACTORY = len(robot), len(factory_flatten)
        next_dist = [0 for _ in range(FACTORY + 1)]
        current = [0 for _ in range(FACTORY + 1)]
        for i in range(ROBOT - 1, -1, -1):
            if i != ROBOT - 1:
                next_dist[FACTORY] = 1e12
            current[FACTORY] = 1e12
            for j in range(FACTORY - 1, -1, -1):
                assign = (abs(robot[i] - factory_flatten[j]) + next_dist[j + 1])
                skip = current[j + 1]
                current[j] = min(assign, skip)
            next_dist = current[:]
        return current[0]


if __name__=="__main__":
    sol = Solution()
    
    print(sol.minimumTotalDistance([0,4,6], [[2,2],[6,2]]))
    print(sol.minimumTotalDistance([1,-1], [[-2,1],[2,1]]))