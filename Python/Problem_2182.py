from collections import Counter
import heapq

# Problem - 2583. Kth Largest Sum in a Binary Tree
# Python3 Solution!
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        max_heap = [(-ord(c), cnt) for c, cnt in Counter(s).items()]
        heapq.heapify(max_heap)
        
        res = []
        while max_heap:
            c, cnt = heapq.heappop(max_heap)
            cur = min(cnt, repeatLimit)
            res.append(chr(-c) * cur)
            if cnt > cur and max_heap:
                nxt_c, nxt_cnt = heapq.heappop(max_heap)
                res.append(chr(-nxt_c))
                if nxt_cnt > 1:
                    heapq.heappush(max_heap, (nxt_c, nxt_cnt - 1))
                heapq.heappush(max_heap, (c, cnt - cur))
        return "".join(res)


if __name__=="__main__":
    sol = Solution()
    
    print(sol.repeatLimitedString("cczazcc", 3))
    print(sol.repeatLimitedString("aababab", 2))