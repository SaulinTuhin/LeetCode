import heapq
from typing import List

# Problem - 1942. The Number of the Smallest Unoccupied Chair
# Python3 Solution!
class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        idx_map = [i for i in range(len(times))]
        idx_map.sort(key = lambda i : times[i][0])
        
        occupied_chairs = [] # (leave time, chair no.)
        available_chairs = [i for i in range(len(times))] # chair no.
        
        for i in idx_map:
            arrival_t, leave_t = times[i]
            while occupied_chairs and occupied_chairs[0][0] <= arrival_t:
                l_time, chair = heapq.heappop(occupied_chairs)
                heapq.heappush(available_chairs, chair)
                
            chair = heapq.heappop(available_chairs)
            heapq.heappush(occupied_chairs, (leave_t, chair))
            
            if i == targetFriend:
                return chair
        return -1
    

if __name__=="__main__":
    sol = Solution()
    
    print(sol.smallestChair([[1,4],[2,3],[4,6]], 1))
    print(sol.smallestChair([[3,10],[1,5],[2,6]], 0))