import heapq

# Problem - 1405. Longest Happy String
# Python3 Solution!
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = ""
        maxHeap = []
        if a: heapq.heappush(maxHeap, (-a, 'a'))
        if b: heapq.heappush(maxHeap, (-b, 'b'))
        if c: heapq.heappush(maxHeap, (-c, 'c'))
        
        while maxHeap:
            count, char = heapq.heappop(maxHeap)
            if not count:
                break
            if len(res) > 1 and res[-2] == res[-1] == char:
                if not maxHeap:
                    break
                count2, char2 = heapq.heappop(maxHeap)
                res += char2
                count2 += 1
                if count2:
                    heapq.heappush(maxHeap, (count2, char2))
            else:
                res += char
                count += 1
            if count:
                heapq.heappush(maxHeap, (count, char))
        return res
    
    
if __name__=="__main__":
    sol = Solution()
    
    print(sol.longestDiverseString(1, 1, 7))
    print(sol.longestDiverseString(7, 1, 0))